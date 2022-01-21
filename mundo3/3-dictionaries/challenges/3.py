#!/usr/bin/python
print ("""092
Read name, date of birth and work id. Record age, based on birthday. If work id !=0 will also record the year o hiring and salary.
Calculate, despite of age, how old he/she will retire
""")

worker={}

worker['name']
worker['date_birth']
worker['labor_id'] = int(input("Enter your Labor ID (0 if you don't have): "))
if worker['labor_id'] != 0:
  worker['labor_year'] = int(input("Enter year you've started working: "))
  worker['labor_salary'] = int(input("Enter your salary: "))