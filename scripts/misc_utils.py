#!/usr/bin/python
# File Name : scripts/misc_utils.py
# Creation Date : Sat Apr 23 13:59:53 2011
# Last Modified : Sat Apr 23 14:10:55 2011
# Created By :  Lane Smith

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
    if not path.exists('avida'):
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
