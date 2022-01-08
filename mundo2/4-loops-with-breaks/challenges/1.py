#!/usr/bin/python
print ("""066
Read int numbers. Stop when number=999. 
Then show how much numbers were typed and sum
""")

s=count=0
while True:
    n = int(input("Enter a number [999 to stop]: "))
    if n == 999:
        break
    count+=1
    s+=n
print("{} numbers were typed and the sum of them is {}".format(count,s))