#!/usr/bin/python

print("""018
COMPOSED VARIABLES - LISTS Part 2

Lists into Lists

data = []
# ADDING
data.append("Peter")
data.append("25")
#["Peter",25]

people=[]
people.append(data[:]) #Copy from data an agreate as a list into a list

people=[["Peter",25],["Mary",19],["John",32]]
print(people[0][0]) # Peter
print(people[1][1]) # 19
print(people[1]) # ['Maria', 19]


test =[]
test.append("Andre")
test.append(33)
crowd.append(test) # !!!
test[0]="Mary"
test[1]=22
crowd.append(test)
print(crowd)
# [['Mary',22],['Mary',22]]

test =[]
test.append("Andre")
test.append(33)
crowd.append(test[:])# !!!
test[0]="Mary"
test[1]=22
crowd.append(test[:])
print(crowd)
# [['Andre',33],['Mary',22]]

new_crew = [['John', 19],['Anne', 33],['Doug',41],['Maicon',35]]
print(new_crew[0][1]) #19
print(new_crew[2][1]) #41
print(new_crew[[3][0]) #41

for p in new_crew:
    print(p)

crew = list()
data = []
for d in range(0,5):
    data.append(str(input("Name: ")))
    data.append(str(input("Age: ")))
    crew.append(data[:])
    data.clear()
print(crew)

totm=totminor=0
for p in crew:
    if p[1] >= 21:
        print(f"{p[0]} is major age")
        totm+=1
    else:
        print(f"{p[0]}")
        totminor+=1

print(f"You have {totm} major age and {totminor} minors")

""")
crew = list()
data = []
for d in range(0,5):
    data.append(str(input("Name: ")))
    data.append(int(input("Age: ")))
    crew.append(data[:])
    data.clear()
print(crew)

totm=totminor=0
for p in crew:
    if p[1] >= 21:
        print(f"{p[0]} is major age")
        totm+=1
    else:
        print(f"{p[0]} is minor")
        totminor+=1

print(f"You have {totm} major age and {totminor} minors")
print(len(crew))