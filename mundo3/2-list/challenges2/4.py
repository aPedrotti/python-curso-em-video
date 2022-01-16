#!/usr/bin/python
print ("""087
Improvement of 086 showing:
Sum of all evens numbers
Sum of ll values of the thrird column
Highest number of second line
""")
matrix = [[],[],[]]
odds=third_column=higher=0

for l in range(0,3):
    for c in range(0,3):
        matrix[l].append(int(input(f"Enter number for the [[{l},{c}] position: ")))
        if matrix[l][c] % 2 == 0:
            odds+=matrix[l][c]
        if c == 2:
            third_column+=matrix[l][c]
        if l == 1:
            if matrix[l][c] > higher:
                higher=matrix[l][c]

print("-="*10)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matrix[l][c]:^5}] ",end=" ")
    print()

print("-="*10)
print("Sum of all evens numbers is: ",odds)
print("Sum of all values of the Third Column is: ",third_column)
print("The higher number of the second line is: ",higher)