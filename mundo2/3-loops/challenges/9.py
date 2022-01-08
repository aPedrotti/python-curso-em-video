#!/usr/bin/python
print ("""
Read numbers and check avg between, which was the highest and the lowest until user confirms would like to continue
""")

c='Y'
count=s=0
highest=1
lowest=99999
while c == 'Y':
    n = int(input("Enter a value: "))
    count+=1
    s+=n
    if n > highest:
        highest=n 
    if n < lowest:
        lowest=n
    c = str(input("Would like to continue? [Y/N] ")).upper()
print("The avg of all numbers is: {:.2f}".format(s/count))
print("The Highest number was {} and the Lowest was {}".format(highest,lowest))