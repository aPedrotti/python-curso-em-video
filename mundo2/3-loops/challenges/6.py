#!/usr/bin/python
print ("""062
Redo the previous (PA) asking how much terms would like to see or 0 to stop
""")

s = int(input("Enter Start: "))
j = int(input("Enter Jump: "))
term=s
count=1
total=0
rep=10
while rep !=0:
    total+=rep
    while count <= total: 
        print(term,"->",end=" ")
        term+=j
        count+=1
    print("PAUSE")
    rep = int(input("How much terms would like to show? "))
print("Finish with {} terms".format(total))
