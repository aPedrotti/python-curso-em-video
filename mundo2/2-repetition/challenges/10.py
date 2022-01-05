#!/usr/bin/python
weights=5
print ("""
Read {} weights and tell which was the highest and the lowest 
""".format(weights))
highest = 0
lowest = 0
for i in range(0,weights):
    if i == 0:
        highest = w
        lowest = w
    w = float(input("Enter a weight: "))
    if w > highest:
        highest=w
    elif w < lowest:
        lowest=w
print("The Highest: ",highest)
print("The Lowest: ",lowest)