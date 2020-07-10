import requests
import random
def main():
    r = requests.get('https://cat-fact.herokuapp.com/facts')
    for catfact in r.json()["all"]:
        print(catfact.get("text"))
        print(random.choice(r.json()["all"])["text"])
main()
