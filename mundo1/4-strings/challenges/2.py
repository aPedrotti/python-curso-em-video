#!/usr/bin/python

print("""Create a program that reads number between 
0 and 9999 and shows each digit splitted 
Ex: 1834
Unit: 4
Ten: 3
Hunders: 8
Thousands: 1
""")

number = str(input('Enter a number between 0 and 9999: '))

# Mathematical way of doing
u = number // 1 % 10
t = number // 10 % 10
h = number // 100 % 10
t = number // 1000 % 10

print('Unit: {}'.format(u))
print('Ten: {}'.format(t))
print('Hunders: {}'.format(h)) 
print('Thousands: {}'.format(t))