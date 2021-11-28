#!/usr/bin/python

print("""Create a program that reads a full name and then shows:
- Name with all caps
- Name with all lower
- How much chars (do not consider spaces)
- How much chars has the first name
""")

name = str(input('Type your Full Name: '))

print(name.upper())
print(name.lower())
print(len(name.strip()))
words = name.split()
print(len(words[0]))