#!/usr/bin/env python3
import requests
uri="https://www.anapioficeandfire.com/api"
def main():
    res=requests.get(uri)
    #decode the response
    got_dj=res.json()
    ##print respose
    print(got_dj)

main()
