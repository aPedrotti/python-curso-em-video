#!/usr/bin/python
print ("""080
Read 5 numbers and add at same index (do not use sort).
Shows (ordered) list
""")

number=0
repetitions=5
values=list()

for i in range(0,repetitions):
  number = int(input(f"Enter {i}/{repetitions-1} number: "))
  print(number)
  if i == 0 or number > values[-1]:
    values.append(number)
    print(f"Inserted number {number} at position {i} ")
  else:  
    pos = 0
    while pos < len(values):
      if number <= values[pos]:
        values.insert(pos, number)
        break
      pos+=1
    print(f"Inserted number {number} at position {pos} ")
print("-="*10)

print(values)