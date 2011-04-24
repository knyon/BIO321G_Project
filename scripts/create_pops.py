#!/usr/bin/python
# File Name : scripts/create_pops.py
# Creation Date : Wed Apr 20 14:10:41 2011
# Last Modified : Sun Apr 24 16:38:37 2011
# Created By :  Lane Smith

# This script automatically creates the population files required for the
# experiment using avida. This script should be run inside the 'scripts'
# directory, and the 'scripts' directory should be on the same tree level as
# the 'avida' directory.


import os, shutil
from os import path
# Module is scripts/misc_utils.py
from misc_utils import verify_file_locs, move_file, display_msg, run_avida

EVN = "environment.cfg" 
CUSTOM_EVNS = ["native_environment.cfg", "invasive_environment.cfg"]  # Required configuration files for this script
AVIDA_DIR = path.join(os.pardir, 'avida') # Relative location of the avida directory


verify_file_locs(CUSTOM_EVNS, AVIDA_DIR)
seed = input("Please enter the seed number (digits of UT EID): ")
username = raw_input("Please enter your first name: ").lower()

if path.exists(EVN):  # If there already exists an environment.cfg file, move it out of the way
    os.rename(EVN, "temp")

for cfg in CUSTOM_EVNS:
    run = 1
    run_avida(cfg, seed)
    display_msg("Run "+str(run) +" of avida completed.")
    run += 1

    data_src = path.join('data','detail-100000.spop')
    data_dest = path.join(os.pardir, 'saved_data', username)
    dest = move_file(data_src, data_dest)
    display_msg("File "+data_src+" moved to "+dest)


if path.exists("temp"):  # Put back the environment.cfg file
    os.rename("temp", EVN)
display_msg("Script has finished.")
