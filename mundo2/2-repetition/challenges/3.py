#!/usr/bin/python
print ("""
Sum all ODDs that are multiples of three between 1 and 500
""")
c = 0
s = 0
for i in range(1,501):
    if i % 2 !=0 and i % 3 == 0:
        c = c + 1
        s = s + i
print("Sum of all '{}' multiples of 3 ODD's numbers is: {}".format(c,s))
