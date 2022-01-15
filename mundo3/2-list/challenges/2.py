#!/usr/bin/python
print ("""079
Enter N (wants to continue?) values to a list. If number exists, do not consider.
Shows numbers in progressive order
""")
number=0
numbers=[]
while True:
  number = int(input("=== Enter a number: "))
  if number not in numbers:
    numbers.append(number)
    print("Added successfuly",number)
  else:
    print("- Number already exists. Not included")
  cont = str(input("Want to continue? [Y/N] ")).strip().upper()[0]
  if cont == "N":
    break
#numbers.sort()
print("Sorted numbers are ",sorted(numbers))