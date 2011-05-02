#!/usr/bin/python
# This script automatically creates the population files required for the
# experiment using avida. This script should be run inside the 'scripts'
# directory, and the 'scripts' directory should be on the same tree level as
# the 'avida' directory.


import os, shutil
from os import path
# Module is scripts/helper_functions.py
from helper_functions import verify_file_locs, move_files, display_msg, run_avida

EVN = "environment.cfg" 
CUSTOM_EVNS = ["native_environment.cfg", "invasive_environment.cfg"]  # Required configuration files for this script
AVIDA_DIR = path.join(os.pardir, 'avida') # Relative location of the avida directory


verify_file_locs(CUSTOM_EVNS, AVIDA_DIR)
seed = input("Please enter the seed number (digits of UT EID): ")
username = raw_input("Please enter your first name: ").lower()

move_files("temp", EVN) # If there already exists an environment.cfg file, move it out of the way

try:
    for cfg in CUSTOM_EVNS:
        run = 1
        run_avida(seed)
        display_msg("Run "+str(run) +" of avida completed.")
        run += 1

        data_src = path.join('data','detail-100000.spop')
        data_dest = path.join(os.pardir, 'saved_data', username)
        dest = move_files(data_dest, data_src)
finally:
    move_files(os.curdir, path.join("temp", EVN))
display_msg("Script has finished.")
