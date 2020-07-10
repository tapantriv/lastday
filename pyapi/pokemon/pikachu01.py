#!/usr/bin/python3

import requests

# define base URL
POKEURL = "http://pokeapi.co/api/v2/pokemon/"
def main():
    pokemon=requests.get(f'{POKEURL}?limit=1000')
    pokemon= pokemon.json()
      # Loop through data, and print pokemon names
    for poke in pokemon["results"]:
          # Display the value associated with 'name'
          print(poke.get("name"))
    print(f"Total number of Pokemon returned:{len(pokemon['results'])}")
if __name__ == "__main__":
    main()
