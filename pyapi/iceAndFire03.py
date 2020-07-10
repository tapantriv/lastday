import requests
uri="https://www.anapioficeandfire.com/api/books"
def main():
    res=requests.get(uri)
    #Decoding Here
    response= res.json()
    for single in response:
        print(f"{single['name']},pages-{single['numberOfPages']}" )
        print(f"\tapiURL -> {single['url']}\n")
        print(f"ISBN{single['isbn']}\n")
        print(f"\tPublisher - >{single['publisher']}\n")
        print(f"\tNO.of character->{len(single['characters'])}\n")

main()
