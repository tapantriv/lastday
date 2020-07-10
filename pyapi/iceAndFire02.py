import pprint
import requests
baseurl= "https://www.anapioficeandfire.com/api/books"
def main():
    res = requests.get(baseurl)
    dj=res.json()
    pprint.pprint(dj)

main()

