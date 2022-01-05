#!/usr/bin/python
print ("""
Read high and weight, calculates 'IMC' and tells if:
<18.5           - Under weight
>=18.5 and <25  - Right weight
>=25 and <30    - Over Weight
>=30 and <40    - Too Over weight
>=40            - You are going to die :(
""")

colours = {"red": "\033[30;41m",
            "green": "\033[30;42m",
            "yellow": "\033[30;43m",
            "offwhite": "\033[7m",
            "clean": "\033[m"}

high = float(input("Enter how high you are: (use DOT as separator) "))
weight = float(input("Enter you weight you are: (use DOT as separator) "))

imc = weight / (high ** 2)
print ("Your IMC is: {:.1f}".format(imc))
if imc < 18.5:
    print("{}Under Weight{}".format(colours["yellow"],colours["clean"]))
elif 18.5<= imc < 25:
    print("{}Right Weight{}".format(colours["green"],colours["clean"]))
elif 25<= imc < 30:
    print("{}Over Weight{}".format(colours["yellow"],colours["clean"]))
elif 30<= imc < 40:
    print("{}Too Over Weight{}".format(colours["red"],colours["clean"]))
else:    
    print("{}You are going to die {}".format(colours["offwhite"],colours["clean"]))
