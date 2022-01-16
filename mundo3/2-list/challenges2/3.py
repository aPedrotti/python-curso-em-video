#!/usr/bin/python
print ("""086
read 9 numbers and fill a matrix 3x3
Example:
[ 1 ][ 2 ][ 3 ]
[ 4 ][ 5 ][ 6 ]
[ 7 ][ 8 ][ 9 ]
""")
main = [[],[],[]]
number = 0

for i in range(0,3):
    main[0].append(int(input(f"Enter number for the [[0,{i}]th position: ")))
for i in range(0,3):
    main[1].append(int(input(f"Enter number for the [[1,{i}]th position: ")))
for i in range(0,3):
    main[2].append(int(input(f"Enter number for the [[2,{i}]th position: ")))

for i in main[0]:
    print(f"[ {i} ] ",end=" ")
for i in main[1]:
    print(f"[ {i} ] ",end=" ")
for i in main[2]:
    print(f"[ {i} ] ",end=" ")