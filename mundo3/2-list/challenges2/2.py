#!/usr/bin/python
print ("""
Read 7 numbers and and in a list and keep odds and evens split
Show Odds and evens, sorted 
""")
main=[[],[]]
number = 0
for i in range(1,8):
    number = int(input(f"Enter number ID {i}: "))
    if number % 2 == 0:
        main[0].append(number)
        print("Evens: ",main[0])
    else:
        main[1].append(number)
        print("Odds: ",main[1])
print("-="*10)
# main[0].sort()
# main[1].sort()
#print("Evens: ",main[0])
#print("Odds: ",main[1])
print("Evens: ",sorted(main[0]))
print("Odds: ",sorted(main[1]))