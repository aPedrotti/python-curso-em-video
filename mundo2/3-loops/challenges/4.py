#!/usr/bin/python
from math import factorial

print ("""060
Read a number and shows its "factorial"
ex:
5!=5*4*3*2*1=120

""")

n = int(input("Enter a number: "))
f=n
fact=1
print("Calculating {}! ..." )
while f > 0:
    print("{}".format(f),end="")
    print(" x " if f > 1 else " = ", end="")
    fact*=f
    f-=1
print("{}".format((fact)))
print("{}".format(factorial(n)))