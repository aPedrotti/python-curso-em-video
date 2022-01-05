#!/usr/bin/python
print ("""
Read 2 numbers, compare them and say who is higher, lower or if they are equal
""")

n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

if n1 > n2:
    print("{} is higher then {}".format(n1,n2))
elif n2 > n1:
    print("{} is higher then {}".format(n2,n1))
else:
    print("Numbers are equal")