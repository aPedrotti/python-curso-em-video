#!/usr/bin/python
print ("""
Show all even numbers between 1 and 50 
""")

for i in range(1,51):
    if i % 2 == 0:
        print("Number {} is even! ".format(i))