#!/usr/bin/python
from datetime import date
print ("""
Read a persons age and tells if he will serve to army, he has to sign or if his period is expired.
Also say how much time (expired or to)
""")
army_age=18
current_year=date.today().year
birth = int(input("Enter birth year: "))
age = current_year-birth

if age > army_age:
    print("You have pass your time assingment in {} years".format(age-army_age))
    print("You SHOULD HAVE sign in by {}".format(current_year-(age-army_age)))
elif age < army_age:
    print("You have {} years until signment".format(army_age-age))
    print("You sign in by {}".format(current_year+(army_age-age)))
else:
    print("You are in the year of signment. Please check your local army to sign up")
