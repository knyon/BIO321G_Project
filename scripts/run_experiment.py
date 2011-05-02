#!/usr/bin/python
# This script automatically runs the experiment by using the population files
# created with the create_pops.py script. This script should be run inside the
# 'scripts' directory, and the 'scripts' directory should be on the same tree
# level as the 'avida' directory.

import os, shutil, re
from os import path
# Module is scripts/misc_utils.py
from misc_utils import verify_file_locs, move_files, display_msg, run_avida

AVIDA_DIR = path.join(os.pardir, 'avida') # Relative location of the avida directory
EVENTS = "events.cfg"
EVN = "environment.cfg" 
ANALYZE = "analyze.cfg"
CUSTOM_EVENTS = ["experiment_events.cfg"]
CUSTOM_EVNS = ["invasive_environment.cfg", "native_environment.cfg"]  # Required configuration files for this script
CUSTOM_ANALYZE = ["invasive_analyze.cfg"]
POPULATION_FILES = ["native-detail-100000.spop", "invasive-detail-100000.spop"]


# move the population files
username = raw_input("Please enter your first name or the name of the directory\nin the 'saved_data' directory: ").lower()
user_pops_dir = path.join(os.pardir, 'saved_data', username)
user_pop_files = []
for pop in POPULATION_FILES:
    user_pop_files.append(path.join(user_pops_dir,pop))

required_files = CUSTOM_EVENTS + CUSTOM_EVNS + CUSTOM_ANALYZE + user_pop_files
verify_file_locs(required_files, AVIDA_DIR)
moved_cfgs = move_files("temp", EVN, ANALYZE) # If there already exists configuration files, move them out of the way
moved_pop_files = move_files(os.curdir, *user_pop_files)

try:
    os.rename(CUSTOM_EVNS[0], EVN)
    os.rename(CUSTOM_ANALYZE[0], ANALYZE)
    # find the dominant sequence
    run_avida(-1)
    display_msg("Analysis complete")
    moved_cfgs += move_files("temp", EVENTS)
    os.rename(ANALYZE, CUSTOM_ANALYZE[0])

    with open("data/dom_genotype.dat") as fp:
        for line in fp:
            if re.match(r'[^#]\w+', line):
                dom_genotype = line.strip()
                break
        
    # edit the events.cfg file
    with open("experiment_events.cfg") as fp:
        detail_line = re.compile(r"(.*InjectSequence\s)(\w+)")
        fo = open("events.cfg", "w")
        for line in fp:
            if detail_line.match(line):
                line = detail_line.sub(r'\1'+dom_genotype+'\n',line)
            fo.write(line)
        fo.close()

    os.rename(EVN,CUSTOM_EVNS[0])
    os.rename(CUSTOM_EVNS[1], EVN)
    run_avida()
    os.rename(EVN, CUSTOM_EVNS[1])

    save_data_path = path.join(os.pardir, "saved_data", username, "experimental_data")
    data_files = []
    for f in os.listdir("data"):
        if fi not in ['README', '.DS_store']:
            data_files.append(path.join("data",f))
    move_files(save_data_path, *data_files)

finally:
    if path.exists(EVENTS):
        os.remove(EVENTS)
    move_files(os.curdir, *moved_cfgs)  # Move all of the configuration files back
    move_files(user_pops_dir, *moved_pop_files)
display_msg("Script has finished.")
