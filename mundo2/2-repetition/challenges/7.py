#!/usr/bin/python
print ("""
Read a int number and tells if prime number (divisible by 1 and itself)
""")

num = int(input("Enter a number: "))
colours= {"green": "\033[32m",
            "red": "\033[31m",
            "offwhite": "\033[7m",
            "clean": "\033[m"}
c = 0
for i in (range(1,num+1)):
    if num % i == 0:
        print("{}{}{}".format(colours["green"],i,colours["clean"]),end=" ")
        c = c + 1
    else:
        print("{}{}{}".format(colours["red"],i,colours["clean"]),end=" ")
print("\nNumber {} was divisible {} times.".format(num,c))
if c == 2:
    print("That's why it is considered {}PRIME{}".format(colours["offwhite"],colours["clean"]))
else:
    print("So it is {}NOT Prime{}".format(colours["offwhite"],colours["clean"]))