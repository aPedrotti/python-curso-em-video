#!/usr/bin/python
from random import randint
from time import sleep


print ("""088
Ask how much tickets of lotery will be generated (6 numbers / 1-60) (can´t repeat numbers)
record them in a multi-list 

""")

tickets = int(input("How much bets would like to random? "))
game=list()
games=list()
num=count=total=0
while total <=tickets:
    while True:
        for g in range(0,6):
            num = randint(1,60)
            if num not in game:
                game.append(num)
                count+=1
        game.sort()
        games.append(game[:])
        game.clear()
        if count >= 6:
            break
    total+=1

print("$"*21)
print("{:^4}".format("Python Lotery"))
print("$"*21)
print("-="*3,f"Getting lucky numbers of your {tickets} games","-="*3)
for i in range(0,tickets):
    print(f"Bet {i+1}: ",games[i])
    sleep(1)
print("-="*5,f" GOOD LUCK ","-="*3)
