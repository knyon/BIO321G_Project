#!/usr/bin/python
# File Name : scripts/create_pops.py
# Creation Date : Wed Apr 20 14:10:41 2011
# Last Modified : Sat Apr 23 12:13:39 2011
# Created By :  Lane Smith

import os, shutil
from os import path

EVN = "environment.cfg" 
CUSTOM_EVNS = ["control_environment.cfg", "treatment_environment.cfg"]  # Required configuration files for this script
AVIDA_DIR = path.join(os.pardir, 'avida') # Relative location of the avida directory

def verify_file_locs(required_files):
    if not path.exists(AVIDA_DIR):
        print "Script has not been run in the right location. Please run this in a directory whose parent directory contains the directory 'avida'."
        exit()
    os.chdir(AVIDA_DIR)
    if not path.exists('avida'):
        print "The 'avida' executable does not exist in the 'avida' directory."
        exit()
    missing = []
    for f in required_files:
        if not path.exists(f):
            missing.append(f)
    if missing:
        print "The folder is missing the following configuration files required for this script:", missing

def run_avida(cfg, seed):
    os.rename(cfg, EVN)  
    os.system("./avida -s " + str(seed) + " > "+os.devnull)  # Execute avida with the given seed. Throw output into the bit bucket.
    os.rename(EVN, cfg)

def move_file(src, dest_dir):

    if not path.exists(dest_dir):
        os.mkdir(dest_dir)

    filename, ext = path.splitext(src)
    end_count = 1
    while path.exists(path.join(dest_dir, filename+ext):
        end_str = str(end_count)
        if filename.endswith("_"+end_str):
            filename = filename[:-len(end_str)]
        else:
            filename += "_"
        filename += end_str
        end_count +=1

    shutil.move(src, path.join(dest_dir, filename+ext)

def display_msg(msg):
    if os.name == 'posix' AND path.exists('/usr/local/bin/growlnotify'): # If the OS is Mac OS X and has growlnotify installed, print the message using growlnotify
        os.system("growlnotify -m '"+msg+"' -s")
    else:
        print msg


verify_file_locs(CUSTOM_EVNS)
seed = input("Please enter the seed number: ")

if path.exists(EVN)     # If there already exists an environment.cfg file, move it out of the way
    os.rename(EVN, "temp")
for cfg in CUSTOM_EVNS:
    run_avida(cfg)
    move_file(path.join('data','detail-100000.spop')
if path.exists("temp"):  # Reset the environment.cfg file
    os.rename("temp", EVN)
display_msg("Script has finished.")
