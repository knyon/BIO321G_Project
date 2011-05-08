# BIO 321G Final Project --- Invasive Avida Study

##About

All data, scripts, and executables in this repository are for the Spring 2011
BIO 321G Final Project. Various output data was also added to this repository
to distribute amoung group members. This repository is self contained. No other
files are necessary to download, including the avida executables. 

##Requirements

While several attempts were made at making this project cross-platform,
unfortunately, the Windows API for avida makes this impossible at this time.
This should work on all POSIX and \*nix systems, though it has only been tested
on Mac OS X. Python 2.6 or later is required. This scripts will not work with
Python 3. 

##Installation 

Download the entire repository using the _Download_ link at the top of this
GitHub page and extract the archive. Alternatively, use _git clone_ and clone
this repository using the associated URL, also at the top of the page.

##Running the Experiment

Change your working directory to the _scripts_ directory. The scripts will not
run from any other directory.

1. **Create native and invasive populations.**
    Run the create\_pops.py script using any Python interpreter.
    Enter your name when prompted and the digits of your UTEID (or any other
    digits). Your data will be saved in the directory *saved_data/yourname* and
    the digits are the random seed used for avida. It will output the two 
    populations to this directory.
    
2. **Run the experiment.**
    Run the run\_experiment.py script using any Python interpreter. Enter your
    name when prompted, or the name of the directory containing invasive and
    native populations in the *saved_data/their_name* directory (e.g., _nedu_,
    _sarah_, or _lane). The script looks for population files in the
    *saved_directory/yourname* directory. The script will perform several trials
    and will save the data from each trial in the *saved_data/yourname* directory,
    with the data from each trial in it's own directory titled
    *experimental_data_[0-9]+*.

##License

We claim no warranty on anything in this repository. Use at your own risk. Feel 
free to use and modify the scripts at will. The avida software has it's own 
license, which is available at
https://github.com/devosoft/avida-core/blob/master/COPYING.
