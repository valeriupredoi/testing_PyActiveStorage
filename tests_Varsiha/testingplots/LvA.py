import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from matplotlib.lines import Line2D
import sys
from pathlib import Path
import importlib.util

sys.path.append("..") 
plt.rcParams['font.family'] = 'Arial'

import importlib.util
from pathlib import Path


def getVals(path, array_name="real_times"):
    """
    Load a Python file at 'path' as a module and return the specified array.
    
    Parameters:
        path (str): Path to the Python file
        array_name (str): Name of the array variable to import (default 'real_times')
    
    Returns:
        np.array: The requested array from the file
    """
    file_path = Path(path)
    spec = importlib.util.spec_from_file_location("module_from_file", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    return getattr(module, array_name)

# --- 1. INPUT YOUR INDIVIDUAL NP ARRAYS HERE ---
# (Replace these placeholders with your actual numpy arrays)

t1_Local   = getVals("../output/Local_v_Active/Target1_Local_f_ch330a.pc19790301_bnl.nc_var_UM_m01s16i202_vn1106_slice_0_8_0_413_0_551_20260330_131924.py"      , "real_times") 
t5_Local   = getVals("../output/Local_v_Active/Target5_Local_f_ch330a.pc19790301_bnl.nc_var_UM_m01s16i202_vn1106_slice_0_14_0_707_0_942_20260330_134057.py"     , "real_times")  
t10_Local  = getVals("../output/Local_v_Active/Target10_Local_f_ch330a.pc19790301_bnl.nc_var_UM_m01s16i202_vn1106_slice_0_18_0_891_0_1188_20260330_142336.py"   , "real_times")  
t25_Local  = getVals("../output/Local_v_Active/Target25_Local_f_ch330a.pc19790301_bnl.nc_var_UM_m01s16i202_vn1106_slice_0_25_0_1209_0_1612_20260330_145609.py"  , "real_times")  
t50_Local  = getVals("../output/Local_v_Active/Target50_Local_f_ch330a.pc19790301_bnl.nc_var_UM_m01s16i202_vn1106_slice_0_31_0_1525_0_2032_20260330_154812.py"  , "real_times")
t75_Local  = getVals("../output/Local_v_Active/Target75_Local_f_ch330a.pc19790301_bnl.nc_var_UM_m01s16i202_vn1106_slice_0_36_0_1753_0_2337_20260330_164934.py"  , "real_times")  


t1_Active  = getVals("../output/Local_v_Active/Target1_Active_f_ch330a.pc19790301_bnl.nc_var_UM_m01s16i202_vn1106_slice_0_8_0_413_0_551_20260330_130305.py"     , "real_times")
t5_Active  = getVals("../output/Local_v_Active/Target5_Active_f_ch330a.pc19790301_bnl.nc_var_UM_m01s16i202_vn1106_slice_0_14_0_707_0_942_20260330_135715.py"    , "real_times")  
t10_Active = getVals("../output/Local_v_Active/Target10_Active_f_ch330a.pc19790301_bnl.nc_var_UM_m01s16i202_vn1106_slice_0_18_0_891_0_1188_20260330_140024.py"  , "real_times") 
t25_Active = getVals("../output/Local_v_Active/Target25_Active_f_ch330a.pc19790301_bnl.nc_var_UM_m01s16i202_vn1106_slice_0_25_0_1209_0_1612_20260330_165917.py" , "real_times") 
t50_Active = getVals("../output/Local_v_Active/Target50_Active_f_ch330a.pc19790301_bnl.nc_var_UM_m01s16i202_vn1106_slice_0_31_0_1525_0_2032_20260330_165647.py" , "real_times")  
t75_Active = getVals("../output/Local_v_Active/Target75_Active_f_ch330a.pc19790301_bnl.nc_var_UM_m01s16i202_vn1106_slice_0_36_0_1753_0_2337_20260330_165353.py" , "real_times")   

arr_L4_on,  arr_L4_off = np.array([1,2,3]),    np.array([1,2,3])

# --- 2. STRUCTURE INTO CUSTOM DATA ---
# Format: [ [Data_ON], [Data_OFF], "Label" ] -> Position Swapped per request
custom_data = [
    ((np.array([]), np.array([]), "")) ,
    (t1_Active  ,t1_Local   ,  "1%  "),
    (t5_Active  ,t5_Local   ,  "5%  "),
    (t10_Active ,t10_Local  ,  "10% "),
    (t25_Active ,t25_Local  ,  "25% "),
    (t50_Active ,t50_Local  ,  "50% "),
    (t75_Active ,t75_Local  ,  "75% "),
    (arr_L4_on, arr_L4_off, "100% ")
    ]

SHOW_VIOLINS = True 

def plot_dual_hybrid_row(ax, y_pos, data_on, data_off, show_violins=SHOW_VIOLINS):
    # Swapped order: ON is first (lower), OFF is second (higher)
    colors = ["#fd5400", "#939393"] 
    datasets = [data_on, data_off]
    
    if len(data_on) == 0 or len(data_off) == 0:
        return  # skip empty row

    for i, data in enumerate(datasets):
        color = colors[i]
        # Offset 0.1 for the first element (ON), 0.5 for the second (OFF)
        offset = 0.1 if i == 0 else 0.5
        
        mean = np.mean(data)
        std = np.std(data)
        
        if show_violins:
            kde = stats.gaussian_kde(data)
            x_range = np.linspace(min(data) - std, max(data) + std, 100)
            kde_values = (kde(x_range) / max(kde(x_range))) * 0.35 
            
            ax.fill_between(x_range, y_pos + offset, y_pos + offset + kde_values, alpha=0.2, color=color)
            ax.plot(x_range, y_pos + offset + kde_values, color=color, lw=1)

        # Plot Error Bars
        ax.errorbar(mean, y_pos + offset, xerr=std, fmt='o', color=color, 
                    elinewidth=2.5, capsize=4, markersize=8, zorder=3)

# --- Plotting Logic ---
fig, ax = plt.subplots(figsize=(12, 8)) # Widened slightly for text space

y_ticks, y_labels = [], []



for i, (d_on, d_off, label) in enumerate(custom_data):
    # CHANGE 1: Skip the empty placeholder so 1% starts at the bottom
    if i == 0:
        continue 
    
    # CHANGE 2: Simplified y_pos (i * 1.5) makes it build from bottom (1%) to top (100%)
    y_pos = i * 1.5
    
    plot_dual_hybrid_row(ax, y_pos, d_on, d_off)
    
    y_ticks.append(y_pos + 0.3)
    y_labels.append(label)

    # CHANGE 3: Logic for dotted lines (Draw ABOVE the current row)
    # This skips the line for the very top (100%) row
    if i < len(custom_data) - 1:
        ax.axhline(y_pos + 1.15, color="#bbbbbb", lw=1.5, linestyle=':')

    # --- STATS TEXT ON THE RIGHT ---
    if len(d_on) > 0 and len(d_off) > 0:
        mean_on, std_on = np.mean(d_on), np.std(d_on)
        mean_off, std_off = np.mean(d_off), np.std(d_off)
        
        ratio = mean_off / mean_on
        ratio_std = ratio * np.sqrt((std_off/mean_off)**2 + (std_on/mean_on)**2)
        
        labels_text = "Active:\nLocal:\nRatio:"
        values_text = (
            f"{mean_on:>7.2f} ± {std_on:>5.2f}\n"
            f"{mean_off:>7.2f} ± {std_off:>5.2f}\n"
            f"{ratio:>7.2f} ± {ratio_std:>5.2f}"
        )

        # Labels (Arial)
        ax.text(0.835, y_pos + 0.3, labels_text, 
                transform=ax.get_yaxis_transform(),
                fontsize=12, va='center', ha='right')

        # Values (Monospace for ± alignment)
        ax.text(0.84, y_pos + 0.3, values_text, 
                transform=ax.get_yaxis_transform(),
                fontsize=12, va='center', ha='left', 
                family='monospace')


"""
for i, (d_on, d_off, label) in enumerate(custom_data):
    # Adjust spacing
    if i == 0:
        y_pos = (len(custom_data) - i) * 1.5 + 1.5
    else:
        y_pos = (len(custom_data) - i) * 1.5
    
    plot_dual_hybrid_row(ax, y_pos, d_on, d_off)
    
    y_ticks.append(y_pos + 0.3)
    y_labels.append(label)

    if (i>0) and (i < len(custom_data) - 1):
        ax.axhline(y_pos - 0.25, color="#bbbbbb", lw=1.5, linestyle=':')

    # --- ADDED: STATS TEXT ON THE RIGHT ---
    if len(d_on) > 0 and len(d_off) > 0:

        mean_on, std_on = np.mean(d_on), np.std(d_on)
        mean_off, std_off = np.mean(d_off), np.std(d_off)
        
        # Calculate Ratio
        ratio = mean_off / mean_on
        
        # Calculate Propagated Uncertainty for the ratio
        # Formula: ratio * sqrt((std_off/mean_off)^2 + (std_on/mean_on)^2)
        ratio_std = ratio * np.sqrt((std_off/mean_off)**2 + (std_on/mean_on)**2)
        
        # Construct the string with \pm symbols



        labels = "Active:\nLocal:\nRatio:"
        values = (
            f"{mean_on:>7.2f} ± {std_on:>5.2f}\n"
            f"{mean_off:>7.2f} ± {std_off:>5.2f}\n"
            f"{ratio:>7.2f} ± {ratio_std:>5.2f}"
        )

        # 1. The Labels (Standard Font, Right Aligned)
        ax.text(0.835, y_pos + 0.3, labels, 
                transform=ax.get_yaxis_transform(),
                fontsize=12, va='center', ha='right')

        # 2. The Values (Monospace Font, Left Aligned)
        # Shift the x-coordinate (0.84) slightly to the right of the labels
        ax.text(0.84, y_pos + 0.3, values, 
                transform=ax.get_yaxis_transform(),
                fontsize=12, va='center', ha='left', 
                family='monospace')
"""


"""
        stats_text = (
            f"{'Active:':<{lbl_w}} {mean_on:>{val_w}.2f} ± {std_on:>{unc_w}.2f}\n"
            f"{'Local:':<{lbl_w}} {mean_off:>{val_w}.2f} ± {std_off:>{unc_w}.2f}\n"
            f"{'Ratio:':<{lbl_w}} {ratio:>{val_w}.2f} ± {ratio_std:>{unc_w}.2f}"
        )

        # We place this at the far right of the current axis
        # 'transform=ax.get_yaxis_transform()' means x is in Axes coords (0-1), y is in Data coords
        ax.text(0.83, y_pos + 0.3, stats_text, 
                transform=ax.get_yaxis_transform(),
                fontsize=12, va='center' )

"""

# --- EXTEND AXIS ---
# Get current max and extend it by 25% to fit the labels inside the box
current_xmax = ax.get_xlim()[1]
print ("current_xmax",current_xmax)
ax.set_xlim(10, 900*3) 


ax.set_ylim(1.0, (len(custom_data) * 1.5) + 1.5)
ax.set_xscale('symlog', linthresh=30)

# Styling
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_labels, fontsize=12, ha='right')
ax.tick_params(axis='y', length=0, pad=20)
ax.set_xlabel('Execution Time (seconds)', fontsize=12)
ax.spines[['top', 'right', 'left']].set_visible(True)

# Legend
legend_elements = [
    Line2D([0], [0], color="#fd5400", marker='o', lw=2, label='Active Storage'),
    Line2D([0], [0], color='#939393', marker='o', lw=2, label='Local Storage ')
]
ax.legend(handles=legend_elements, loc='upper right', frameon=False, fontsize=12,  bbox_to_anchor=(0.95, 0.96))

# Bold header text
ax.text(0.01, 0.98, "Reduction execution time relative to slice size",
    fontsize=12, fontweight='bold', va='top', ha='left', transform=ax.transAxes)

ax.text(0.01, 0.945, 
    "File: ch330a.pc19790301-bnl.nc\nVariable: UM_m01s16i202_vn1106\n3400 Chunks, 17.96 GB",
    fontsize=12, fontweight='normal', va='top', ha='left', linespacing=1.5, transform=ax.transAxes)

plt.tight_layout()
plt.savefig("ExecutionTime_Local_v_Active.pdf")

