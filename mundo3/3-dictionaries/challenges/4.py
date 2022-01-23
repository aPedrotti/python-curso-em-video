#!/usr/bin/python
print ("""093
Read a soccer player name and how much matches he played.
Then reads how much goals he/she scored for each match. It all be recorded in a dict including total goals during championship 

""")

player={}
goals=[]
player['name'] = str(input('Player Name: '))
player['matches'] = int(input('How much matches: '))
for i in range(1,player['matches']+1):
    goals.append(int(input(f'How much goals at match {i} ')))
player['goals'] = goals.copy()
player['total_goals'] = sum(goals)
print('-='*10)
print(player)
print('-='*10)
for k,v in player.items():
    print(f" Field {k} has value {v}")
print('-='*10)
print(f"Player '{player['name']}' played '{len(player['goals'])}' matches")
for i,v in enumerate(player['goals']):
    print(f"   At match {i+1} he scored {v}")
print(f" Total Goals {player['total_goals']}")
