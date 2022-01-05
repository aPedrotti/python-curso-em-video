#!/usr/bin/python
print ("""
Read the first term and reason of a "Arthimetic Progression" then show the first 10 values
""")
s = int(input("Enter Start: "))
j = int(input("Enter Jump: "))
for i in range(s,j*10,j):
    print(i,"->",end=" ")
print("Finish")