#!/usr/bin/python
print ("""081
Read N numbers to a list and then:
How many numbers were typed, ordered list reverse, if number 5 were typed or not in the list
""")
number=num_five=0
numbers=[]
while True:
    number = int(input("Insert a number: "))
    numbers.append(number)
    if number == 5:
        
    cont = str(input("Do you want to continue? [Y/N] ")).strip().upper()[0]
    if cont == "N":
        break
print("-="*10)
print(f"You typed {len(numbers)} numbers")
print(f"The reverse order is: {sorted(numbers,reverse=True)}")
if num_five == 0:
    print("Number 5 was not added")
else:
    print(f"Number 5 was typed {num_five} times")