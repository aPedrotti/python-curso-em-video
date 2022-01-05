#!/usr/bin/python
print ("""
Recap exercise 009 and create a times table using loop 
""")
n = int(input("Enter a number to get its times table: "))

for i in range(1,11):
    print("{} x {} = {}".format(n,i,n*i))