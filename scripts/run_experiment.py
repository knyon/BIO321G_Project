#!/usr/bin/python
# File Name : scripts/run_experiment.py
# Creation Date : Sat Apr 23 13:53:22 2011
# Last Modified : Sat Apr 23 22:31:52 2011
# Created By :  Lane Smith

import os, shutil, re
from os import path
# Module is scripts/misc_utils.py
from misc_utils import verify_file_locs, move_file, display_msg

AVIDA_DIR = path.join(os.pardir, 'avida') # Relative location of the avida directory
EVENTS = "events.cfg"
CUSTOM_EVENTS = ["experiment_events.cfg"]


# move the population files
verify_file_locs(CUSTOM_EVENTS, AVIDA_DIR)
username = raw_input("Please enter your first name or the name of the directory\nin the 'saved_data' directory: ").lower()

if path.exists(EVENTS):  # If there already exists an environment.cfg file, move it out of the way
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
    os.rename("temp", EVN)
