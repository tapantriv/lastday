#!/usr/bin/env python3
round =0
while True:
    round = round + 1
    print('Finish the movietitle, "Monty Python\'s the Life of ______"i')
    answer = input("Your guess-->")
    if answer == 'Brian':
                print("correct")
                break;
    elif round ==3:
                print("Sorry , the answer was Brain.")
                break
    else:
                print("Sorry! Try again")

