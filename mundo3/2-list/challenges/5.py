#!/usr/bin/python
print ("""082
Read N values to a list;
Create 2 new lists for placing odds and evens numbers
""")

number=0
numbers=[]
odds=[]
evens=[]
while True:
  number = int(input("Insert a number: "))
  numbers.append(number)
  odds.append(number) if number % 2 == 0 else evens.append(number)
  cont = str(input("Do you want to continue? [Y/N] ")).strip().upper()[0]
  if cont == "N":
    break


print(f"All Numbers are: {sorted(numbers)}")
print(f"Odds Numbers are: {sorted(odds)}")
print(f"Evens Numbers are: {sorted(evens)}")