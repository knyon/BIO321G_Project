#!/usr/bin/python
# File Name : scripts/run_experiment.py
# Creation Date : Sat Apr 23 13:53:22 2011
# Last Modified : Sun Apr 24 18:37:15 2011
# Created By :  Lane Smith

# This script automatically runs the experiment by using the population files
# created with the create_pops.py script. This script should be run inside the
# 'scripts' directory, and the 'scripts' directory should be on the same tree
# level as the 'avida' directory.

import os, shutil, re
from os import path
# Module is scripts/misc_utils.py
from misc_utils import verify_file_locs, move_file, display_msg, run_avida

AVIDA_DIR = path.join(os.pardir, 'avida') # Relative location of the avida directory
EVENTS = "events.cfg"
EVN = "environment.cfg" 
ANALYZE = "analyze.cfg"
CUSTOM_EVENTS = ["experiment_events.cfg"]
CUSTOM_EVNS = ["invasive_environment.cfg"]  # Required configuration files for this script
CUSTOM_ANALYZE = ["invasive_analyze.cfg"]
POPULATION_FILES = ["native-detail-100000.spop", "invasive-detail-100000.spop"]


# move the population files
username = raw_input("Please enter your first name or the name of the directory\nin the 'saved_data' directory: ").lower()
user_pops_dir = path.join(os.pardir, 'saved_data', username)
user_pop_files = []
for pop in POPULATION_FILES:
    user_pop_files.append(path.join(user_pops_dir,pop))
    
verify_file_locs(CUSTOM_EVENTS + CUSTOM_EVNS + CUSTOM_ANALYZE +user_pop_files, AVIDA_DIR)

if path.exists(EVENTS):  # If there already exists an events.cfg file, move it out of the way
    os.rename(EVENTS, "temp")

# find the dominant sequence
for cfg in CUSTOM_EVNS:
    run_avida(cfg, EVN)
    display_msg("Analysis complete")

with open("data/dom_genotype.dat") as fp:
    for line in fp:
        if line[0] != "#" and len(line) > 10:
            dom_genotype = line.strip()
            break

    
# edit the events.cfg file
with open("experiment_environment.cfg") as fp:
    detail_line = re.compile(r"(.*InjectSequence\s)(\w+)")
    fo = open("environment.cfg", "w")
    for line in fp:
        if detail_line.match(line):
            line = detail_line.sub(r'\1'+dom_genotype+'\n')
        fo.write(line)
    fo.close()



if path.exists("temp"):  # Put back the environment.cfg file
    os.rename("temp", EVENTS)
display_msg("Script has finished.")
