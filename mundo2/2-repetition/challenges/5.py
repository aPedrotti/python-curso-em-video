#!/usr/bin/python
print ("""
read 6 int numbers and sum only those EVEN. If Odd, discart
""")
c=0
s=0
for i in range(1,7):
    num = int(input("Enter the {}th number: ".format(i)))
    if num %2 == 0:
        c = c + 1
        s = s + num
print("Sum of all {} Even number is: {}".format(c,s))