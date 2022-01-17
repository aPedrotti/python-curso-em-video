#!/usr/bin/python
print ("""089
Read N names and 2 scores in a multi-list 
Show avg of of each and ask if wants to show scores of someone 
Example:
Id. NAME    AVG
------------------
0   Anne    5.8
1   John    7.8
2   Mary    9.9
------------------
Wants to see from which student? (999 to quit): 

""")
student=[]
students=[]
number=0
while True:
    student.append(str(input("Name: ")))
    student.append(float(input("1st Grade: ")))
    student.append(float(input("2st Grade: ")))
    cont = str(input("Would like to continue? [Y/N] ")).strip().upper()[0]
    if cont == "N":
        break

print("-"*20)
print("{:2} {} {}".format("No"))
for p in range(0,len(students)): 
    if p % 2 == 0:
        print(f"{students[p]:.<30}",end=" ")
    else:
        print(f"$ {students[p]:>7.2f}")
print("-"*20)

while True:
    number = int(input("Wants to see from which student? (999 to quit): "))
    if cont == 999:
        break
    else:
        #print(f"Grades from {students[student[number][0]]} are: ",students[student[number][1]],students[student[number][2]])
        print("Else")