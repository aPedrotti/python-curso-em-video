#!/usr/bin/python
print ("""063
Read an int number 'n' and shows the 'n' first elements of Fibonacci Sequence 
ex: -
""")

n = int(input("Enter how much terms of Fibonacci would like to see: "))
count=1
v1=0
v2=1
v3=0
while count <=n:
    if v1 == 0:
        print(v1,"->",v2,end=" ")
    else:
        print("->",v3,end=" ")
    v3=v1+v2
    v1=v2
    v2=v3
    count+=1
print("-> END")