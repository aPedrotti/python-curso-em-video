#!/usr/bin/python
print ("""064
read int numbers and only stops when user types '999'.
At the end shows how numbers were typed and which was the sum of them (dismissing scape number)
""")

c=s=0
while c != 999:
    n = int(input('Enter a value [999 to exit]: '))
    if n == 999:
        c = n
        print("Exiting ...".format(c))
    else:
        s +=n
        c+=1
print("Sum of all {} values typed is {}",format(c,s))