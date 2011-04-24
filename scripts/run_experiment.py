#!/usr/bin/python
# File Name : scripts/run_experiment.py
# Creation Date : Sat Apr 23 13:53:22 2011
# Last Modified : Sun Apr 24 13:32:56 2011
# Created By :  Lane Smith

# This script automatically runs the experiment by using the population files
# created with the create_pops.py script. This script should be run inside the
# 'scripts' directory, and the 'scripts' directory should be on the same tree
# level as the 'avida' directory.

import os, shutil, re
from os import path
# Module is scripts/misc_utils.py
from misc_utils import verify_file_locs, move_file, display_msg

AVIDA_DIR = path.join(os.pardir, 'avida') # Relative location of the avida directory
EVENTS = "events.cfg"
CUSTOM_EVENTS = ["experiment_events.cfg"]
POPULATION_FILES = ["native-detail-100000.spop", "invasive-detail-100000.spop"]


# move the population files
username = raw_input("Please enter your first name or the name of the directory\nin the 'saved_data' directory: ").lower()
user_pops_dir = path.join(os.pardir, 'saved_data', username)
user_pop_files = []
for pop in POPULATION_FILES:
    user_pop_files.append(path.join(user_pops_dir,pop))
    
verify_file_locs(CUSTOM_EVENTS + user_pop_files, AVIDA_DIR)

if path.exists(EVENTS):  # If there already exists an events.cfg file, move it out of the way
    os.rename(EVENTS, "temp")

# find the dominant sequence

# edit the events.cfg file
    # remove previous
    # add new sequence
# loop
    # run experiment
    # move files to save data
# 
if path.exists("temp"):  # Put back the environment.cfg file
    os.rename("temp", EVENTS)
display_msg("Script has finished.")
