
#!/bin/bash
python plot_time2.py -i  ../output/f_ch330a.pc19790301-def.nc_var_UM_m01s16i202_vn1106_MT_100_Net_UoREth_Slice_0_30_0_30_0_30.py \
                     -o  hist_f_ch330a.pc19790301-def.nc_var_UM_m01s16i202_vn1106_MT_100_Net_UoREth_Slice_0_30_0_30_0_30.pdf



python plot_time2.py -i ../output/f_cl_Amon_UKESM1-0-LL_ssp370SST-lowNTCF_r1i1p1f2_gn_205001-209912.nc_var_cl_MT_100_Net_UoREth_Slice_0_30_0_30_0_30.py \
    -o hist_f_cl_Amon_UKESM1-0-LL_ssp370SST-lowNTCF_r1i1p1f2_gn_205001-209912.nc_var_cl_MT_100_Net_UoREth_Slice_0_30_0_30_0_30.pdf

python plot_time2.py -i ../output/f_da193a_25_6hr_t_pt_cordex__198807-198807.nc_var_m01s30i111_MT_100_Net_UoREth_Slice_0_30_0_30_0_30.py\
    -o hist_f_da193a_25_6hr_t_pt_cordex__198807-198807.nc_var_m01s30i111_MT_100_Net_UoREth_Slice_0_30_0_30_0_30.pdf

python plot_time2.py -i ../output/f_da193a_25_day__198808-198808.nc_var_m01s06i247_4_MT_100_Net_UoREth_Slice_0_30_0_30_0_30.py\
    -o hist_f_da193a_25_day__198808-198808.nc_var_m01s06i247_4_MT_100_Net_UoREth_Slice_0_30_0_30_0_30.pdf