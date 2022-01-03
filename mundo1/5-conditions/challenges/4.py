#!/usr/bin/python

print ("""
Calculates travel bill charging 0.5 / km up to 200 km and 0.45 for above
""")

colours = {'clean':'\033[m',
        'white':'\033[7m',
        'blue':'\033[44m',
        'green':'\033[30;42m',
        'warning':'\033[0;30;43m',
        'alert':'\033[0;30;41m'}

distance = float(input('How far are you going to travel: '))

if distance <= 200:
    cost = distance*0.5
    print('Since your travel is up to 200 it will cost {}${:.2f}{}'.format(colours['green'],cost,colours['clean']))
else:
    cost = distance*0.45
    print('Since your travel is above 200 it will cost {}${:.2f}{}'.format(colours['green'],cost,colours['clean']))
print("Can also be calculated as: 'cost = distance * 0.50 if distance <= 200 else distancia * 0.45 '") 
