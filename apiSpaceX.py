#!/usr/bin/python3
"""
Author: RZFeeser
This program harvests SpaceX data avail from https://api.spacexdata.com/v3/cores using the Python Standard Library methods
"""

# using std library method for getting at API data
import urllib.request 
import json

# GOBAL / CONSTANT of the API we want to lookup
SPACEXURI = "https://api.spacexdata.com/v3/cores"

def main():
    count=0
    # create a urllib.request response object by sending an HTTP GET to SPACEXURI
    coreData = urllib.request.urlopen(SPACEXURI)

    # pull STRING data off of the 200 response (even tho it's JSON!)
    xString = coreData.read().decode()
    print(type(xString))

    # convert STRING data into Python Lists and Dictionaries
    listOfCores = json.loads(xString)
    print(type(listOfCores))

    for core in listOfCores:
   #     print(core, end="\n\n")
        count= count+0
        print(core['core_serial'])
        print(core['original_launch'],end='\n\n')
        print(F'total count is {count}')

 
      # you pressed ctrl S, which is old school LINUX command to STOP SCREEN
        # way back in the day before linux was "good" you had to freeze the screen when stuff started scroll past too fast
        # to UNFREEZE the screen, use CTRL + Q
    



if __name__ == "__main__":
    main()
