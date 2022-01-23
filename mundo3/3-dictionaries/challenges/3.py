#!/usr/bin/python
print ("""092
Read name, date of birth and work id. Record age, based on birthday. If work id !=0 will also record the year o hiring and salary.
Calculate, despite of age, how old he/she will retire
""")
from datetime import date
today = date.today()
worker={}
age = 0
worker['name'] = str(input("Enter your name: "))
worker['year_birth'] = int(input("Enter you year of birth: "))
worker['labor_id'] = int(input("Enter your Labor ID (0 if you don't have): "))
if worker['labor_id'] != 0:
  worker['labor_year'] = int(input("Enter year you've started working: "))
  worker['labor_salary'] = int(input("Enter your salary: "))
  age = today.year - worker['year_birth']
  worker['retire_year'] = worker['labor_year'] - worker['year_birth'] + 35

print(f"Name is {worker['name']} ")
print(f"You are {age} years old")
print(f"Labor ID {worker['labor_id']}")
print(f"Hire year {worker['labor_year']}")
print(f"Salary was {worker['labor_salary']}")
print(f"Retire when you are {worker['retire_year']} years old")