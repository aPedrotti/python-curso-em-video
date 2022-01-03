#!/usr/bin/python
from random import randrange
from time import sleep
print ("""
Reads a number tries to discovery what the computer has (btw 0-5) and congratulate if find 
""")
computer_number = randrange(6)

print('-=-'*20)
print('I am going to thin a number between 0 and 5. Try to guess...')
print('-=-'*20)

num = int(input('What number did I think? ' ))
print('Comparing...')
sleep(3)

if num == computer_number:
    print('Congratulations you found my number ! ')
else:
    print('Your guess was wrong')
    print('I though on {}'.format(computer_number))

