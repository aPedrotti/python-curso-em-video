#!/usr/bin/python

print("""Create a program that reads a full name and shows: 
- First Name;
- Last name;
""")

name = str(input("Enter your full name:")).split()

total_names = len(name)
print("Total Names: {}".format(total_names))

first_name = name[0]
print("First Name:  {}".format(first_name))

last_name = name[total_names-1]
print("Last Name:   {}".format(last_name))