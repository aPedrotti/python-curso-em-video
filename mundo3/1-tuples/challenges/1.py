#!/usr/bin/python
print ("""072
Tuple with the name of the numbers from 0 to 20. Users enters a number and get its name. Validate if numbers is out range
""")

number=-1
numbers = ("zero","one","two","three","four","five","six","seven","eight","nine","ten",
"eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")

while True:
    number = int(input("Enter a number between 0 and 20: "))
    while 0 <= number >= 20:
        print("Number out of range")
        number = int(input("Enter a number between 0 and 20: "))
    print(f"Written for of {number} is - '{numbers[number]}'")
    cont=" "
    while cont not in "YN":
        cont = str(input("Would like to continue? [Y/N] ")).strip().upper()[0]
    if cont == "N":
        break
print("Finished. Thanks for trying ")