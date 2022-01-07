#!/usr/bin/python

print("""
FOR is when you have limits.
WHILE is for the rest and some of Fors. When you don´t know the limits

while not apple:
    if coin:
        catch
    if floor:
        step
    if hole:
        jump
catch
=====

for c in range(1,10):
    print(c)
print(´Fim')

c=1
while c < 10:
    print(c)
    c += 1

n=1
evens = odds = 0
while n !=0:
    n = int(input('Enter a value: ')) # Will ask until you type 0 (condition)
    if n !=0:
        if n % 2 == 0:
            evens+=1
        else:
            odds+=1
print('You have entered {} numbers Evens and {} Odds'.format(evens,odds))

c='Y'
while c == 'Y':
    n = int(input('Enter a value: ')) # Will ask until you type 0 (condition)
    c = str(input('Would like to continue? [Y/N] )).upper()
print('End')

""")
