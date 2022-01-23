#!/usr/bin/python
print ("""094
Read name, sex and age of people (wants to continue?).
Record each in a dicts and all in a list
How much people were recorded
Age avg
list with all women
list of all people above avg age
""")

people=[]
person={}

while True:
    person['name'] = str(input("Name: "))
    person['sex'] = str(input("Sex: [M/F] ")).strip().upper()[0]
    person['age'] = int(input("Age: "))
    people.append(person[:])
    cont = str(input("Would like to continue? [Y/N] ")).strip().upper()[0]
    if cont == "N":
        break
print("-="*10)
for i,v in enumerate(people):
    for k,v in person.items():
        print(f"{k} = {v}")
print(people)
