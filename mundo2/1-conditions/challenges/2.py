#!/usr/bin/python
print ("""
Read a number and ask if you wants to covert to:
1 - Binary
2 - Octal
3 - Hexa
    or
all 
""")

number = int(input("Enter a number: "))
option = str(input("Enter your option: "))

if option == "1":
    print ("Your number in BIN is {}".format(bin(number)[2:]))
elif option == "2":
    print ("Your number in OCT is {}".format(oct(number)[2:]))
elif option == "3":
    print ("Your number in HEX is {}".format(hex(number)[2:]))
elif option == "all":
    print ("Your number in BIN is {}".format(bin(number)[2:]))
    print ("Your number in OCT is {}".format(oct(number)[2:]))
    print ("Your number in HEX is {}".format(hex(number)[2:]))
else:
    print("Wrong option. It was supposed to be 1, 2, 3 or all")