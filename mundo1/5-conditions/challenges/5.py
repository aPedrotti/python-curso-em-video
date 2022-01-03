#!/usr/bin/python
print ("""
Read a calendar year and tell if it is leap year 
""")

from datetime import date

year = int(input('Enter a year o 0 to current: '))

if year == 0:
    year = date.today().year

if ((year % 4 == 0) 
    and (year % 100 !=0) 
    or (year % 400 == 0)):
    print('Year {} IS Leap Year'.format(year))
else:
    print('Year {} IS NOT Leap Year'.format(year))

print(date.today())