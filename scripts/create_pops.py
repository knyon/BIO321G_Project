#!/usr/bin/python
# File Name : scripts/create_pops.py
# Creation Date : Wed Apr 20 14:10:41 2011
# Last Modified : Thu Apr 21 21:12:12 2011
# Created By :  Lane Smith

import os
import shutil
from os.path import exists

EVN = "environment.cfg"
CUSTOM_EVNS = ["control_environment.cfg", "treatment_environment.cfg"]

def verify_file_locs(required_files):
    if not exists('../avida'):
        print "Script has not been run in the right location. Please run this in a directory whose parent directory contains the directory 'avida'."
        exit()
    os.chdir('../avida')
    if not exists('./avida'):
        print "The 'avida' executable does not exist in the 'avida' directory."
        exit()
    missing = []
    for f in required_files:
        if not exists(f) or not :
            missing.append(f)
    if missing:
        print "The folder is missing the following configuration files required for this script:", missing

def run_avida(cfg, seed):
    os.rename(cfg, EVN)
    if "WINDOWS":
        dest = "something"
    else:
        dest = " > /dev/null"
    os.system("./avida -s "+seed+dest)
    os.rename(EVN, cfg)

def move_file(src, dest_dir):
    if not exists(dest_dir):
        os.mkdir(dest_dir)
    filename = src
    end_count = 1
    while exists(dest+"/"+filename):
        filename +=str(end_count)
        end_count +=1
    shutil.move(src, dest_dir+'/'+filename)


verify_file_locs(CUSTOM_EVNS)
seed = input("Please enter the seed number: ")
if exists(EVN):
    os.rename(EVN, "temp")
for cfg in CUSTOM_EVNS:
    run_avida(cfg)
    if not move_file("data/dat")

os.rename("treatment_environment.cfg", EVN)
os.system("./avida -s "+seed+" > /dev/null")
os.rename(EVN, "treatment_environment.cfg")

if exists(EVN):
    os.rename("temp", EVN)
