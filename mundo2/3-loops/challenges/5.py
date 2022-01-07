#!/usr/bin/python
print ("""
Redo 51 (Progression Arthimetica), reading the first tearm and factor showing the first 10 terms
""")

s = int(input("Enter Start: "))
j = int(input("Enter Jump: "))
c=1
term=s
while c <= 10: 
    print(term,"->",end=" ")
    term+=j
    c+=1
print("Finish")