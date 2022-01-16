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

for l in range(0,3):
    for c in range(0,3):
        main[l].append(int(input(f"Enter number for the [[{l},{c}] position: ")))
        #main[l][c] = int(input(f"Enter number for the [[{l},{c}] position: "))

for l in range(0,3):
    for c in range(0,3):
        print(f"[{main[l][c]:^5}] ",end=" ")
    print()