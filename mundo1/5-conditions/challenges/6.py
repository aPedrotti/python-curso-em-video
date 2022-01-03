#!/usr/bin/python
print ("""
Read 3 numbers and tells which is the higher and the lower 
""")

n1 = int(input('Type the first number: '))
n2 = int(input('Type the second number: '))
n3 = int(input('Type the third number: '))

# Checking the Highest
if n1>n2 and n1>n3:
    highest=n1
if n2>n1 and n2>n3:
    highest=n2
if n3>n1 and n3>n2:
    highest=n3
# Checking the Lowest
if n1<n2 and n1<n3:
    lowest=n1
if n2<n1 and n2<n3:
    lowestt=n2
if n3<n1 and n3<n2:
    lowest=n3

print('The Highest is {}'.format(highest))
print('The Lowest is {}'.format(lowest))