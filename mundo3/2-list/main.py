#!/usr/bin/python

print("""
COMPOSED VARIABLES - LISTS
( ) - tuples
[ ] - lists
{ } - dictionaries

In Lists you can add, remove and update values

meal = list("hamburger","juice","pizza","pudim")
meal = ["hamburger","juice","pizza","pudim"]
meal[3] = "cake" # ["hamburger","juice","pizza","cake"]

print(len(meal)

# ADDING
meal.append("cookie") # Add at the end of the list
#["hamburger","juice","pizza","cake",cookie]

# Defining postion
meal.insert(0,"hotdog")
# ["hotdog","hamburger","juice","pizza","cake",cookie]

# REMOVING
del meal[3] 
meal.pop(3)
# meal.pop() - removes last
meal.remove["pizza"]
# The all update index
if "pizza" in meals:
    meal.remove("pizza")

values = list(range(1,11))
values = ['8','3','4','1','6','2']
values.sort()
values.sort(reverse=True)

for c, v in enumerate(values):
    print(f'At position {c+1} found value {v})

values=list()
for i in range(0,5):
    values.append(int(input("Type a value: ")))

a = [2,1,4,7]
b = a
b[2] = 8
print(f'List A: {a}') #[2,1,8,7]
print(f'List B: {b}') #[2,1,8,7]
# Both lists keeps the same values dispite of the update in B
# Passing a copy of a list:
b = a[:] #'b' receives a copy of all values of 'a'
b[2] = 8
print(f'List A: {a}') #[2,1,4,7]
print(f'List B: {b}') #[2,1,8,7]

""")

