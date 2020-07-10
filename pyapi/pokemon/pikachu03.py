#!/usr/bin/python3

## for accepting arguments from the cmd line
import argparse

## for making HTTP requests
## python3 -m pip install requests
import requests

## for working with data in lots of formats
## python3 -m pip install pandas
import pandas

ITEMURL = "http://pokeapi.co/api/v2/item/"
def main():

    # Make HTTP GET request using requests
    # and decode JSON attachment as pythonic data structure
    # Also, append the URL ITEMURL with a parameter to return 1000
    # items in one response
    items = requests.get (f"{ITEMURL}?limit=1000")
    items = items.json()
     # create a list to store items with the word searched on
    matchedwords = []
      # Loop through data, and print pokemon names
    # item.get("results") will return the list
    # mapped to the key "results"
    if args.searchword in item.get("name"):
         matchedwords.append(item.get("name"))
    finishedlist = matchewords.copy()
    ## map our matchedword list to a dict with a title
    matchedwords = {}
    matchedwords["matched"] = finishedlist
    print(f"There  {len(finishedlist)}  word '{args.searchword}' ")
    print(f"List of Pokemon items containing '{args.searchword}': ")
    print(matchedwords)
     ## export to excel with pandas
    # make a dataframe from our data
    itemsdf = pandas.DataFrame(matchedwords)
    # export to MS Excel XLSX format
    # run the following to export to XLSX
    # python -m pip install openpyxl
    # index=False prevents the index from our dataframe from
    # being written into the data
    itemsdf.to_excel("pokemonitems.xlsx", index=False)
if __name__ == "__main__":
         parser = argparse.ArgumentParser(description="Pass in a word to")
         parser.add_argument('searchword', metavar='SEARCHW',\
         type=str, default='ball', help="Pass in any word. Default is 'ball'")
         args = parser.parse_args()
         main()
