#!/usr/bin/python
print ("""
Jokenpo
""")

from random import choice
from time import sleep
colours = {"red": "\033[30;41m",
            "green": "\033[30;42m",
            "offwhite": "\033[7m",
            "clean": "\033[m"}
print("""
[r] Rock
[p] Paper
[s] Scisor
""")

computer = choice(["r", "p", "s"])    
player = str(input("Make your choice: "))
print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO !")

print("My choice was: {}".format(computer))
if computer == player:
    print("{}DRAW{}".format(colours["offwhite"],colours["clean"]))

elif computer == "r" and player == "p":
    print("You {}WIN{}".format(colours["green"],colours["clean"]))

elif computer == "s" and player == "p":
    print("You {}LOSE{}".format(colours["red"],colours["clean"]))

elif computer == "r" and player == "s":
    print("You {}WIN{}".format(colours["green"],colours["clean"]))

elif computer == "p" and player == "s":
    print("You {}LOSE{}".format(colours["red"],colours["clean"]))

elif computer == "s" and player == "r":
    print("You {}WIN{}".format(colours["green"],colours["clean"]))

elif computer == "p" and player == "r":
    print("You {}LOSE{}".format(colours["red"],colours["clean"]))

else:
    print("There was a choice aside of the expected")
    

