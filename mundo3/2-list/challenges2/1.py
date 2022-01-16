#!/usr/bin/python
print ("""084
Read name and weight and keep them in a list
How much people recorded
Name of people overweight (higher weight)
Name of people underweight (lower weight)

""")

people=[]
person=[]
heavier=lighter=0

while True:
    person.append(str(input("Name: ")))
    person.append(float(input("Weight: ")))
    if len(people) == 0:
        heavier=lighter=person[1]
        print("Currently the heavier and the lightest person is ",person[0])
    else:
        if person[1] > heavier:
            heavier=person[1]
            print("Currently the heavier person is ",person[0])
        if person[1] < lighter:
            lighter=person[1]
            print("Currently the lighter  person is ",person[0])
    people.append(person[:])
    person.clear()
    cont = str(input("Do you want to continue? [Y/N] ")).strip().upper()[0]
    if cont == "N":
        break

print("-="*10)
print(f"There were {len(people)} recorded")

print("-="*10)
print(f"Higher weight was {heavier} from: ",end="")
for p in people:
    if p[1] == heavier:
        print(f"[{p[0]}]",end=(" "))

print("\n","-="*10)
print(f"Ligher weight was {lighter} from: ",end=" ")
for p in people:
    if p[1] == lighter:
        print(f"[{p[0]}]",end=(" "))
