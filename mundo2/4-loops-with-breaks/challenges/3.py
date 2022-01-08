#!/usr/bin/python
print ("""068
Even & Odds game. Stops if player loose and shows how much wins
""")

from random import randint

wins=0
player=" "
print("-=-"*10)
print(" "*8,"ODDS & Even")
print("-=-"*10)
while True:
    number = int(input("Choose a number: "))
    while player not in "OE":
        player = str(input("Odds or Even? [O/E]: ")).strip().upper()[0]
    computer = randint(0,11)
    total = number+computer
    print("Computer: {} / Player: {} = {}".format(computer,number,total))
    print("EVEN" if total % 2 == 0 else "ODDS")
    if total % 2 == 0 and player == "E":
        print("\033[42m*** You WIN ***\033[m")
        wins+=1
    elif total % 2 != 0 and player == "O":
        print("\033[42m*** You WIN ***\033[m")
        wins+=1
    else:
        break
    print("-*- Lets play again -*-")
print("-"*20)
print("\033[41mYou LOST\033[m You won {}".format(wins))
