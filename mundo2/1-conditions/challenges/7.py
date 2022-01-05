#!/usr/bin/python
print ("""
Read 3 sides and tell if it can form a Triangle:
Equilatero  - All sides equals
Isóseles    - 2 sides equals
Escaleno    - All sides differents
""")

s1 = float(input('Enter first size: '))
s2 = float(input('Enter second size: '))
s3 = float(input('Enter third size: '))

if s1 < s2+s3 and s2 < s1+s3 and s3 < s1+s2:
    print('These sizes CAN make a triangle')
    if s1 == s2 and s1 == s3:
        # can also be: if s1 == s2 == s3:
        print("It is an \033[7mEQUILATERO\033[m Triangle")
    elif s1 == s2 or s1 == s3:
        print("It is an \033[7mISOSELES\033[m Triangle")
    elif s1 != s2 and s1 != s3:
        print("It is an \033[7mESCALENO\033[m Triangle")
else:
    print('These sizes CANNOT make a triangle')