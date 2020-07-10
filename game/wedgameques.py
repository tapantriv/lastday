#!/usr/bin/env python3

import requests

def main():
    player= input("Typein you initial")
    rounds=input("Howmany round you like to play?")
    score= 0
    #make requst to http"// jservice.io/api/random
    r = requests.get(f"https://jservice.io/api/random?count={rounds}")
    # strip off JSON from the 


    # display the methods available to our new object

    print("\n\n\n")
    for rand in r.json():
        print(rand['question'])
        (rand['answer'])
        playerans= input("type your answer")
        if playerans.lower() == rand['answer'].lower():
            print("Good job")
            score=score+rand['value']
        else:
            print("Invalid")

    print(f"tap says: let's see how you did \n your scor is {score}" )

    with open ("jscores.txt") as jhs:
        highscore=jhs.readlines()
        highscore.sort()

        for score in highscore:
            if score>higscore:
                print("good")
                highscore.remove(score)
                highscore.append(str(score))
        

main()

