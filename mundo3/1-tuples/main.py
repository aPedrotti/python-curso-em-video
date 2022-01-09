#!/usr/bin/python

print("""
COMPOSED VARIABLES - TUPLES

( ) - tuples
[ ] - lists
{ } - dictionaries

"Tuples are IMUTABLE"
cannot be updated (but can be delete - del(tuple_name))
They can be from differet types of data 

meal = ("hamburger","juice","pizza","pudim")
print(meal[0])   # hamburger
print(meal[0:2]) # hamburger, juice
print(meal[1:])  # juice, pudim
print(meal[-1])  # pudim
print(meal[-2:]) # juice, pizza, pudim
print(len(meal)  # 4
for eat in meal:
    print(f'I am going to eat {eat}')     #hamburger \njuice \npizza \npudim
for eat in range(0,len(meal)):
    print(eat)                            #hamburger \njuice \npizza \npudim
for pos, eat in enumerate(meal):
    print(f'{eat} at position {pos}')     #hamburger \njuice \npizza \npudim

print(sorted(meal))

a = (2,5,4)
b = (5,8,1,2)
c = b + a
print(c) #(5,8,1,2,2,5,4)
print(c.count(5)) #2 
print(c.index(8)) #1
print(c.index(2)) #3

""")
