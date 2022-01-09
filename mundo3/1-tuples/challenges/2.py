#!/usr/bin/python
print ("""073
Tuple of the 20 soccer teams of the current championship 
Shows the top 5, last 4, sort alphabetically, highlight position of the team "chapecoense"
""")

championship = ("Atletico MG","Flamengo","Palmeiras","Fortaleza","Corinthians",
                "Bragantino","Fluminense","America MG","Atletico GO","Santos",
                "Ceara","Internacional","Sao Paulo","Athletico","Cuiaba",
                "Juventude","Gremio","Bahia","Sport","Chapecoense")

print("The Top 5:")
for i in range(0,5):
    print(f"{i+1} - {championship[i]}")
print("-"*20)

print("Worst 4: ")
#for i in range(-len(championship),-5):
print(f"{championship[-4:]}")
print("-"*20)

print("Sort Alphabetically: ")
teams = sorted(championship)
for i in range(0,len(championship)):
    print(f"{teams[i]}")
print("-"*20)

team = "Chapecoense"
print("{} is currently at position: {}".format(team,championship.index(team)+1))
