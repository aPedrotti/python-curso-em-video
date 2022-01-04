#!/usr/bin/python

print("""
"'== Conditionals example: '"
age = int(input("How old is your car: "))
if age <=3:
    print("Your car is NEW")
elif age > 50:
    print("Your car is very rare")
else:
    print("Your car is just OLD")
print("--FINISH--")
""")

age = int(input("How old is your car: "))
if age <=3:
    print("Your car is NEW")
elif age > 50:
    print("Your car is very rare")
else:
    print("Your car is just OLD")

n1 = float(input("Enter Your first score: "))
n2 = float(input("Enter Your second score: "))

average = (n1 + n2)/2
succeded = 7.0
print ("Your average was {}".format(average))
if average <= succeded: 
    print("You FAILED")
    if average <= succeded and average >= succeded-1:
        print("But you were very close")
else:
    print("You SUCCEDED")

print("""--Also works as: 
print("SUCCEDED" if average<= 7.0 else "FAILED")
""")
print("SUCCEDED" if average<=7.0 else "FAILED")
