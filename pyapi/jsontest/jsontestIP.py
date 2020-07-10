#!/usr/bin/python3
import requests
#define the URL
IPURL= "http://ip.jsontest.com/"

def main():
    #use requests library to send an HTTP Get
    resp = requests.get(IPURL)
    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()
    print(respjson)
    #just display the value if "IP"
    print(f"The current WAN IP is -->{respjson['ip']}")
if __name__ =="__main__":
    main()

