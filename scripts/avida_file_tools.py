#need os.walk and re.search
import os, re

from numpy import *

import gzip

def get_dominant_fitness(treatPrefix):

    #list of files that contain detail dumps
    files = []

    #search string to use
    searchStr = treatPrefix+"[0-9a-zA-Z_]*/data"

    #find all dominant output files that match the search string
    for path, names, filename in os.walk('.',False):

        #search the path for the resulting directory
        sPath = re.search(searchStr, path)

        #re.search returns none if it failed
        if(sPath != None):

            #file name contains a list of the files in the directory we found
            #we need to check each one to make sure the outputfile is there
            for file in filename:
                
                if(re.search("dominant\.dat\.gz",str(file)) != None):
                    files.append(path+"/"+file)

    return array(files)

### return a given column from a standard avida file
### 
def get_column(file,col):

    #list of stuff to return
    stuff = []

    #open a gzipped file
    fp = gzip.open(file)

    #dump the entire file into 'data'
    data = fp.readlines()

    #close the filepointers
    fp.close()

    #each line contains a treatement
    for line in data:

        #make sure the line starts with a column
        if(re.search("^[0-9]+", line) != None):
            stuff.append(float(re.split(" ",line)[col-1]))

    return stuff
 
