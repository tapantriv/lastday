#!/usr/bin/python3
import requests
import json
#define URL
GETURL= "http://validate.jsontest.com/"
def main():
    # test data to validate as legal json
    mydata= {"fruit":["apple","pear"],"veg":["carrot"]}
    ## user json library to convert to legal json, then strip out whitespace
    jsonToValidate =f"json= {json.dumps(mydata).replace(' ', '')}"
    # use requests library to send an HTTP GET
    resp= requests.get(f"{GETURL}?{jsonToValidate}")
    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson= resp.json()
    #display our PYTHONICdata(LIS /DICT)
    print(respjson)
    #just display the value of "validate"
    print(f"IS your jaon valid?{respjson['validate']}")
if __name__ == "__main__":
    main()

