#!/usr/bin/env python3
#https://statsapi.web.nhl.com/api/v1/teams
import requests
import json
def main():
    url= "https://statsapi.web.nhl.com/api/v1/teams"
    statUrl=requests.get(url)
    #get all data
    statUrl = statUrl.json()
    #print(statUrl)
    count = 0
    # using for loop to reach team and then get teamNumber
    for x in statUrl["teams"]:
        # adding kind of index so it will print team Name:
        count+=1
        print(f'Team Number {count} and team Name is {x["teamName"]}')
        print(f' sorted {sort_values(x["teamName"])}')
        


if __name__ == "__main__":
    main()
