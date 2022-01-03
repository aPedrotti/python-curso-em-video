#!/usr/bin/python
print ("""
Read a salary and tells how much is the raise. if salary > 1250 raise=10/100 else 15/100
""")

salary = float(input('Enter you salary: $'))
if salary > 1250:
    upgrade = salary*0.1
else:
    upgrade = salary*0.15

print('You will get a raise of ${}. Your new salary is: ${}'.format(upgrade,salary+upgrade))