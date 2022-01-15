#!/usr/bin/python
print ("""078
Read 5 values and keep them in a list. 
Shows which was the higher, the lowest and their respective position on the list 
""")
numbers=5

values=list()
lower_pos=list()
higher_pos=list()
higher=lower=0
for i in range(0,numbers):
  values.append(int(input(f"Enter {i}/{numbers-1} number:")))
  if i == 0:
    higher=lower=values[i]
  else:
    if values[i] > higher:
      higher=values[i]
    if values[i] < lower:
      lower=values[i]

print("\n","-"*10) 
print(f"The Lowest is: {lower} at positions: ",end=(""))
for c, v in enumerate(values):
  if v == lower:
    print(f"{c}... ",end=(""))

print()

print(f"The Highest is: {higher} at positions: ",end=(""))
for c, v in enumerate(values):
  if v == higher:
    print(f"{c}... ",end=(""))
