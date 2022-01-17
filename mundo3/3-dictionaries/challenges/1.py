#!/usr/bin/python
print ("""090
Read name and avg score and also keeps the situation (approved or failed)
Then show the content
Name: 
Avg for <name>: 

Name is <name>
Avg is <avg>
Situation is <Failed/Succeded >=7>

""")

student = {}

student['name'] = str(input("Name: ")).capitalize()
student['score'] = float(input(f"Average Score of {student['name']}: "))
if student['score'] >= 7:
    student['status'] = "Succeded"
elif 5 <= student['score'] < 7:
    student['status'] = "Probation"
else:
    student['status'] = "Failed"

print(f"Student {student['name']}")
print(f"Scored {student['score']}")
print(f"Situation is: {student['status']}")