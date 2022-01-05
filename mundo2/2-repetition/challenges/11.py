#!/usr/bin/python
print ("""
Read Name, Age and Sex of 4 people and tells:
- What is the avg age
- What is the name of the oldest man
- How many women are younger then 20
""")

people=4
ages=0
oldest=0
name_oldest_man=""
c_women=0
for i in range(1,people+1):
    print("-=-"*5,"Enter the name {} ".format(i),"-=-"*5)
    name = str(input("Enter your Name: "))
    age = int(input("Enter your Age: "))
    sex = str(input("Enter your Sex (m/f): "))
    ages += age
    if age > oldest and sex in "Mm":
        name_oldest_man = name
    if sex in "Ff" and age < 20:
        c_women += + 1

print("The average age is: {:.1f}".format(ages/people))
print("The name of the oldest man is: {}. He is {} years old".format(name_oldest_man,oldest))
print("There are {} women younger than 20 years".format(c_women))