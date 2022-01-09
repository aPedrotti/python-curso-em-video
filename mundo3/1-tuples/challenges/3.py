#!/usr/bin/python
print ("""074
random 5 numbers and place in a tuple
show the list, the lowest and the highest
""")

from random import randint

numbers = (randint(1,10), randint(1,10), randint(1,10),
        randint(1,10), randint(1,10))

print("Sorted numbers: ",end="")
for number in numbers:
    print(f"{number}",end=" ")

print("\n","-"*10) 
print(f"The Lowest is: {max(numbers)}")
print(f"The Highest is: {min(numbers)}")