#!/usr/bin/python
print ("""091
4 players rolls a dice (random) and store in a dict
Sort this dict and tell the winner

Plays:
    Player 1 got <number>
    Player 2 got <number>...
Ranking:
    1o place: player3 with 6
    2o place: player4 with 4...
""")

from random import randint
from time import sleep
from operator import itemgetter

game = {'1': randint(1,6),
        '2': randint(1,6),
        '3': randint(1,6),
        '4': randint(1,6)}
ranking = {}
print("-="*10)
for k,v in game.items():
    print(f"Player {k} got {v} number")
    sleep(1)

ranking = sorted(game.items(), key=itemgetter(1), reverse=True) # if 0 ordered by value | Transforms in list
print("-="*10)
print("Winners are... ")
for k,v in ranking:
    print(f"Player {k} who got {v}")
