
import requests
# getting API
baseURL= "https://www.anapioficeandfire.com/api/characters?name="
dj= requests.get(baseURL)
dj
#create a script that accepts input from the user,
userinput= input("what are you looking for?")

#and searches for a particular character.
def main():
    if userinput==dj['name']:
        print("found it")
    else:
        print("Are yousure about name?")

main()
#If found, we can return that character's URL. We can complete this by reading the documentation regrading the character API. The API notes that we can send a parameter name= to perform a search on the available character APIS.
