#!/usr/bin/python
print ("""
Read people sex and accept values as M / F. Case wrong, ask again
""")

sex = str(input('What is your sex? [M/F] ')).strip().upper()[0]
while sex not in "MmFf":
    sex = str(input('Wrong answer. Are you F or M ? ')).strip().upper()[0]
print('Sex {} registered'.format(sex))