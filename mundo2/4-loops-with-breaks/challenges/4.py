#!/usr/bin/python
print ("""069
Read age and sex and ask if want to continue:
Then shows how much people are older than 18, how much men, and how much women younger than 20
""")

count=males=females=0
while True:
    age=0
    while age <= 0:
        age = int(input("Age: "))
    sex=" "
    while sex not in "MF":
        sex = str(input("Male or Female? [M/F]: ")).strip().upper()[0]
    if sex == "F" and age < 20:
        females += 1
    if sex == "M" and age > 18:
        males+=1
    count+=1
    cont=" "
    while cont not in "YN":
        cont = str(input("Wants to continue? [Y/N] ")).strip().upper()[0]
    if cont != "Y":
        break
print("{} people / {} men older than 18 / {} girls younger than 20".format(count,males,females))