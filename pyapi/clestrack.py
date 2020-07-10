#!usr/bin/python3
import requests
import json
import pandas as pd
from flask import Flask
app = Flask(__name__)

page= "http://www.celestrak.com/NORAD/elements/tle-new.txt"
newPage = requests.get(page)
#newPage= newPage.json()
df = pd.read_csv("http://www.celestrak.com/NORAD/elements/tle-new.txt",delimiter=';')

#Decorator
#@app.route("/home")

#def home():
 #   return page

#def main():
 #   print(df)

# This is Decorator for Home Route
@app.route("/home")
def home():
   # return newPage
   # I want to print csv file to my home page
    return df

if __name__ == "__main_":
    app.run(host="0.0.0.0", port=2224)

