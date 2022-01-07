#!/usr/bin/python
print ("""
Improve ex 28 where computer thinks a number btw 0-10 and by the and shows how much guess were taken to discovery
""")

from random import randrange

number_limit=10
computer = randrange(number_limit+1)
c=0

print('-=-'*20)
print('I am going to thin a number between 0 and {}. Try to guess...'.format(number_limit))
print('-=-'*20)
user = int(input('What number did I think? '))

while user != computer:
    c+=1
    if user > computer:
        print("Its Less than that.")
    elif computer > user:
        print("Its More than that")
    user = int(input('Try again: '))
print("You took {} shots to guess".format(c))