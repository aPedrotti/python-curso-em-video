#!/usr/bin/python
from cmath import exp


print ("""083
Reads and expression and tells if it is formated correctly with the parentesis
ex: ((a+b)*c) # Correct
""")

expression = list(str(input("Enter an expression: ")))

if expression.count("(") == expression.count(")"):
    print("It is a VALID Expression!")
else:
    print("It is INVALID Expression!")

#Answer from class
expr=str(input("Enter an expression: "))
pile=[]
for p in expr:
    if p == "(":
        pile.append("(")
    elif p == ")":
        if len(pile) > 0:
            pile.pop()
        else:
            pile.append(")")
            break
if len(pile) == 0:
    print('It is Valid Expression')
else:
    print('It is Invalid Expression')
