#!/bin/bash

# --- CONFIGURATION ---
TARGET_FILE="ch330a.pc19790301-bnl.nc"
TARGET_VAR="UM_m01s16i202_vn1106"
# Define slices as a simple comma-separated string: start,stop,start,stop...
SLICES_STR="0,4,0,30,0,30"
TEST_NO="42"
# Automatically create a unique name for this run
BASE_NAME="f_${TARGET_FILE}_var_${TARGET_VAR}_slice_${SLICES_STR//,/_}"
LOGFILE="output/test${TEST_NO}_${BASE_NAME}.log.output"
PY_OUT="output/test${TEST_NO}_${BASE_NAME}.py"


> "$LOGFILE"

# --- EXECUTION ---
for i in {1..2}
do
  echo "Run $i:" >> "$LOGFILE"
  # Pass the variables to Python here
  /usr/bin/time -l python scripts/run_new_tenancy.py \
    "$TARGET_FILE" \
    "$TARGET_VAR" \
    "$SLICES_STR" >> "$LOGFILE" 2>&1
  
  echo "----------------------" >> "$LOGFILE"
done

# --- POST-PROCESSING ---
python scripts/getResults.py -i "$LOGFILE" -o "$PY_OUT"

echo "Process Complete."
echo "Log: $LOGFILE"
echo "Result: $PY_OUT"