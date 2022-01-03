#!/usr/bin/python
colours = {'clean':'\033[m',
        'white':'\033[7m',
        'blue':'\033[44m',
        'green':'\033[30;42m',
        'warning':'\033[0;30;43m',
        'alert':'\033[0;30;41m'}

print ("""
Check if the number is Even (rest when spliting = 0 )or Odd (rest when spliting = 1)
""")

number = int(input('Enter a number: '))

if (number % 2 ) == 0:
    print('Your number {} is {}EVEN{}'.format(number,colours['blue'],colours['clean']))
else:
    print('Your number {} is {}ODD{}'.format(number,colours['green'],colours['clean']))