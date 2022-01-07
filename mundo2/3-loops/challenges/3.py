#!/usr/bin/python
print ("""059
Read 2 numbers and shows a menu:
[1] sum
[2] multiply
[3] higher
[4] new numbers
[5] quit

""")
n=0
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
while n != 5:
    n = int(input(""" What would like to do? 
    [1] Sum
    [2] Multiply
    [3] Higher
    [4] New numbers
    [5] Quit
    """))
    if n == 1:
        print(">>> {} + {} = {}".format(n1,n2,n1+n2))
    elif n == 2:
        print(">>> {} x {} = {}".format(n1,n2,n1*n2))
    elif n == 3:
        if n1 > n2:
            print(">>> The first number, {}, is the highest".format(n1))
        elif n2 > n1:
            print(">>> The second number, {}, is the highest".format(n2))
        else:
            print(">>> They are even")
    elif n == 4:
        print(">>> Ok lets try again...")
        n1 = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))
    elif n == 5:
        print("Ok. Thanks for joining! ")
    else:
        print(">>> Wrong answer. It was supposed to be simple <<< ")

