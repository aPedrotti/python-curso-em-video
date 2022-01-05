#!/usr/bin/python
print ("""
Read 2 scores of a student and tells if he 
Succeded    -   >=7 
Probation   -   >=5.0 and <= 6.9
Failed      -   < 5.0
""")
succeded = 7.0
colours = {"red": "\033[30;41m",
            "green": "\033[30;42m",
            "yellow": "\033[30;43m",
            "clean": "\033[m"}
n1 = float(input("Enter Your first score: "))
n2 = float(input("Enter Your second score: "))

average = (n1 + n2)/2
print ("Your average was {}".format(average))
if average < succeded: 
    if average < succeded and average >= 5.0:
        print("{}You are on probation ! {}".format(colours["yellow"],colours["clean"]))
    else:
        print("{}You FAILED{}".format(colours["red"],colours["clean"]))
else:
    print("{}You SUCCEDED{}".format(colours["green"],colours["clean"]))