#!/usr/bin/python
# This script contains various functions that are used in the various scripts
# written for this project.

import os, shutil
from os import path

# Verify the location of the avida directory, the avida executable, and the
# required files for this script.
def verify_file_locs(required_files, avida_dir):
    if not path.exists(avida_dir):
        print "Script has not been run in the right location. Please run this in a directory whose parent directory contains the directory 'avida'."
        exit()
    os.chdir(avida_dir)
    if not path.exists('avida') and not path.exists('avida.exe'):
        print "The 'avida' executable does not exist in the 'avida' directory."
        exit()
    missing = []
    for f in required_files:
        if not path.exists(f):
            missing.append(f)
    if missing:
        print "The folder is missing the following configuration files required for this script:", missing
        exit()

# Move a file 'src' to directory 'dest_dir'. If directory does not exist,
# create a directory. Add an underscore and an incrementing number if there is
# a naming conflict at the destination.
def move_files(dest_dir, *src_files):
    files_moved = []
    for src in src_files:
        if not path.exists(src):
            continue
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
        files_moved.append(dest)
    return files_moved

# Output a message. If the OS is Mac OS X and has growlnotify installed, print
# the message using growlnotify (which is more noticeable than the terminal)
def display_msg(msg):
    if os.name == 'posix' and path.exists('/usr/local/bin/growlnotify'): # 
        os.system("growlnotify -m '"+msg+"' -s") # -s makes it sticky (doesn't go away until clicked)
    else:
        print msg

# Run the avida command, either in normal mode or analyze mode. If 1 parameter
# is passed or seed = 0, run analyze mode. If not, use the seed given to run an
# instance of avida. Function also renames a given environment file to
# 'environment.cfg', and reverts it back to it's original name
def run_avida(seed=0):
    if seed > 0:
        if os.name == "nt":  # if the OS is Windows based
            command = "avida.exe -s "
        else:
            command = "./avida -s "
        os.system(command + str(seed) + " > "+os.devnull)  # Execute avida with the given seed. Throw output into the bit bucket.
    elif seed == 0:
        if os.name == "nt":  # if the OS is Windows based
            command = "avida.exe "
        else:
            command = "./avida "
        os.system(command + str(seed) + " > "+os.devnull)  # Execute avida with the given seed. Throw output into the bit bucket.
    else:
        if os.name == "nt": 
            os.system("avida.exe -a")
        else:
            print "here!"
            os.system("./avida -a")
