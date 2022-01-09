#!/usr/bin/python
print ("""
Read 4 values and store in a tuple
Shows how much times number 9 appears, which position is the number 3 and which numbers are even
""")

from random import randint

#numbers = (randint(1,10), randint(1,10), randint(1,10),
#        randint(1,10), randint(1,10))
numbers = (int(input("Type a number: ")), int(input("Type a number: ")), int(input("Type a number: ")),
        int(input("Type a number: ")), int(input("Type a number: ")))
        
print(f"Here is the list {numbers}")
print(f"Number 9 appeared {numbers.count(9)} times")
if 3 in numbers:
    print(f"Number 3 is in position: {numbers.index(3)+1}")
else:
    print("Number 3 was not sorted")
print("Numbers that are even: ")
for n in numbers:
    if n % 2 == 0:
        print(n,end=" ")
