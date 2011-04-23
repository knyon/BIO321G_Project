#!/usr/bin/python
# File Name : scripts/create_pops.py
# Creation Date : Wed Apr 20 14:10:41 2011
# Last Modified : Sat Apr 23 12:52:06 2011
# Created By :  Lane Smith

import os, shutil
from os import path

EVN = "environment.cfg" 
CUSTOM_EVNS = ["control_environment.cfg", "treatment_environment.cfg"]  # Required configuration files for this script
AVIDA_DIR = path.join(os.pardir, 'avida') # Relative location of the avida directory


# Verify the location of the avida directory, the avida executable, and the
# required files for this script.
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


# Move a file 'src' to directory 'dest_dir'. If directory does not exist,
# create a directory. Add an underscore and an incrementing number if there is
# a naming conflict at the destination.
def move_file(src, dest_dir):

    if not path.exists(src):
        print "The source file you're trying to move doesn't even exist!"
        exit()

    if not path.exists(dest_dir):
        os.mkdir(dest_dir)

    src_dir, src_file = path.split(src)
    filename, ext = path.splitext(src_file)
    end_count = 1
    while path.exists(path.join(dest_dir, filename+ext)):
        end_str = str(end_count)
        if filename.endswith("_"+end_str):
            filename = filename[:-len(end_str)]  #Remove the digits
        else:
            filename += "_"
        filename += end_str
        end_count +=1

    dest = path.join(dest_dir, filename+ext)
    shutil.move(src, dest)
    return dest

# Output a message. If the OS is Mac OS X and has growlnotify installed, print
# the message using growlnotify (which is more noticeable than the terminal)
def display_msg(msg):
    if os.name == 'posix' and path.exists('/usr/local/bin/growlnotify'): # 
        os.system("growlnotify -m '"+msg+"' -s") # -s makes it sticky (doesn't go away until clicked)
    else:
        print msg


verify_file_locs(CUSTOM_EVNS)
seed = input("Please enter the seed number (digits of UT EID): ")
username = raw_input("Please enter your first name: ").lower()

if path.exists(EVN):  # If there already exists an environment.cfg file, move it out of the way
    os.rename(EVN, "temp")

for cfg in CUSTOM_EVNS:
    run = 1
    run_avida(cfg)
    display_msg("Run "+str(run) +" of avida completed.")

    data_src = path.join('data','detail-100000.spop')
    data_dest = path.join(os.pardir, 'saved_data', username)
    dest = move_file(data_src, data_dest)
    display_msg("File "+data_src+" moved to "+dest)


if path.exists("temp"):  # Put back the environment.cfg file
    os.rename("temp", EVN)
display_msg("Script has finished.")
