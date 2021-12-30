#!/usr/bin/python

word = "SILVA"
print("""Create a program that reads a person name and tells 
whether contains with word '{}'
""".format(word))

name = str(input('Enter your full name: ')).strip()

name = name.upper()
ocurrence = name.count(word)
if ocurrence > 0:
    print("Your name contains the family-name '{}' ! ".format(word))

# Using operator
print("Does your name contains '{}'? {}".format(word, word in name.upper()))
