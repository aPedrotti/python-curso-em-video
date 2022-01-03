#!/usr/bin/python
print ("""
Read 3 sizes and tells if can make a triangle 
""")

s1 = float(input('Enter first size: '))
s2 = float(input('Enter second size: '))
s3 = float(input('Enter third size: '))

if s1 < s2+s3 and s2 < s1+s3 and s3 < s1+s2:
    print('These sizes CAN make a triangle')
else:
    print('These sizes CANNOT make a triangle')