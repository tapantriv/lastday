#!/usr/bin/env python 3
import requests
import json

def main():
    userInput= input("please enter API")
    userResponse= (requests.get(userInput)
    print(userResponse)
   # response= requests.get("http://ip-api.com/json/24.48.0.1")
   # print(f'response for this operation is {response.status_code}')
   # print(response)
    if response == 200:
        return json.loads(userResponse.content.decode('utf-8'))
    


if __name__=="__main__":
    main()


