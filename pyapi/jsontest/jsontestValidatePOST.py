#!/usr/bin/python3

import requests

# define the URL we want to use
POSTURL = "http://validate.jsontest.com/"

def main():
    mydata = {"json": "{'fruit': ['apple', 'pear'], 'veg': ['carrot']}" }
    # use request
    resp = requests.post(POSTURL, data = mydata)
    respjson= resp.json()
    print(respjson)
    print(f"Is your JSON valid? {respjson['validate']}")
if __name__=="__main__":
    main()

