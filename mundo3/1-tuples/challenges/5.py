#!/usr/bin/python
from math import prod


print ("""076
1 Tuple with products and prices
Shows prices tabular like
pen ......... $    1.00
computer .... $ 1140.30
printer ......$  319.20

""")

products=("computer",1250.00,"printer",349.9,"desk",244.3,"mouse",12.3,"keyboard",23.1,"book",8.7,"backpack",34.60)

print("-"*40)
print(f"{'PRICE LIST':^40}")
print("-"*40)
for p in range(0,len(products)): 
    if p % 2 == 0:
        print(f"{products[p]:.<30}",end=" ")
    else:
        print(f"$ {products[p]:>7.2f}")
print("-"*40)