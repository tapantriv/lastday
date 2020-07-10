
#!/usr/bin/env python3
import requests


#get Api
def main():
    r = requests.get("https://jservice.io")
    print(r.json().get("all"))
main()

