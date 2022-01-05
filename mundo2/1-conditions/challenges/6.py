#!/usr/bin/python
print ("""
Categorize swimmers based on their ages:
<=9             - mirim
>9  and <=14    - Infantil
>14 and <=19    - Junior
>19 and <=20    - Senior 
>20 - Master
""")
age = int(input("Enter age: "))

if age <= 9:
    print("Mirim")
elif age <=14:
    print("Infantil")
elif age <=19:
    print("Junior")
elif age <=25:
    print("Senior")
elif age > 25:
    print("Master")