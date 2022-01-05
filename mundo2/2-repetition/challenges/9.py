#!/usr/bin/python
people=7
print ("""
Read the birth year of {} people and tell how many reached age of majority
""".format(people))
from datetime import date
current_year=date.today().year
c_min=0
c_maj=0
for i in range(0,people):
    age = int(input("Enter your birth year: "))
    if current_year - age >= 18:
        c_min+=1
    else:
        c_maj+=1

print("{} people reached ane of majority".format(c_maj))
print("{} people is minor".format(c_min))