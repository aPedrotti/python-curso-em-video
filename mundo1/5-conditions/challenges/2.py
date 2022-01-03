#!/usr/bin/python
colours = {'clean':'\033[m',
        'white':'\033[7m',
        'blue':'\033[44m',
        'green':'\033[30;42m',
        'warning':'\033[0;30;43m',
        'alert':'\033[0;30;41m'}

speed_limit=80
speed_charge=7
print ("""
Read a car speed and apply ${} / km above limit ({}km/h)
""".format(speed_charge,speed_limit))

speed = int(input('Enter speed of your vehicle: '))

if speed > speed_limit:
    fee = (speed-speed_limit)*speed_charge
    print('{}You are over the limit{}. You has to pay {}${}{} in charges'.format(colours['alert'],colours['clean'],colours['green'],fee,colours['clean']))
    print('{}Please respect Speed Limits. It is for your safety{}'.format(colours['warning'],colours['clean']))
else:
    print('{}* Thanks for respecting Speed Limits (= *{}'.format(colours['green'],colours['clean']))
print('{}Have a nice have. Drive safe{}'.format(colours['blue'],colours['clean']))

