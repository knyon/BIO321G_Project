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
EVENTS = "events.cfg"
CUSTOM_EVENTS = "create_pop_events.cfg"
AVIDA_DIR = path.join(os.pardir, 'avida') # Relative location of the avida directory


verify_file_locs(CUSTOM_EVNS+[CUSTOM_EVENTS], AVIDA_DIR)
seed = input("Please enter the seed number (digits of UT EID): ")
username = raw_input("Please enter your first name: ").lower()

moved_cfgs = move_files("temp", EVN, EVENTS) # If there already exists an environment.cfg or evemts.cfg file, move it out of the way

try:
    os.rename(CUSTOM_EVENTS, EVENTS)
    for cfg in CUSTOM_EVNS:
        os.rename(cfg, EVN)
        run = 1
        run_avida(seed)
        display_msg("Run "+str(run) +" of avida completed.")
        run += 1
        os.rename(ENV, cfg)

        data_src = path.join('data','detail-100000.spop')
        data_dest = path.join(os.pardir, 'saved_data', username)
        dest = move_files(data_dest, data_src)
        if run == 1:
            os.rename(dest[0],path.join(path.dirname(dest[0]), "native-detail-100000.spop"))
        if run == 2:           #it shouldn't run more than twice, but I don't want it to fail if it does
            os.rename(dest[0],path.join(path.dirname(dest[0]), "invasive-detail-100000.spop"))
finally:
    os.rename(EVENTS, CUSTOM_EVENTS)
    move_files(os.curdir, *moved_cfgs)
display_msg("Script has finished.")
