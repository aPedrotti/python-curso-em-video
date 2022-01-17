#!/usr/bin/python

print("""Class 19
Dictionaries you can name your indexes

d = {}
or
data = dict()

data = {'name':'Peter', 'age': 25}
# key:values
print(data['name'])
print(data['age'])

# To add, Append doesn´t work. 
data['sex']='M'
# Remove
del data['age']

movie={'title':'Star Wars',
        'year':1977,
        'director':'George Lucas'
}
print(movie.keys())   # dict_keys(['title', 'year', 'director'])
print(movie.values()) # dict_values(['Star Wars', 1977, 'George Lucas'])
print(movie.items())  # dict_items([('title', 'Star Wars'), ('year', 1977), ('director', 'George Lucas')])

for k,v in movie.items():
    print(f"The {k} is {v}")

# You can also mix list and dicts 
movie_rent = [{'title':'Star Wars','year':1977,'director':'George Lucas'},{'title':'Avengers','year':2012,'director':'Joss Whedon'},{'title':'Matrix','year':1999,'director':'Wachowski'}]
print(movie_rent[0]['year']) # 1977

people = {'name':'Andre','age':33,'sex':'m'}
print(f"{people['name']} is {people['age']} years old")

for k in people.keys():
    print(f"Key: {k}")      #Key: name, Key: age, Key: sex
for v in people.values(): 
    print(f"Values: {v}")   #Values: Andre, Values: 33, Values: m
for k,v in people.items():
    print(f"{k} = {v}")
people['weight'] = 84.3     #adds a new key and value to people dicts

brazil = []
state1 = {'uf':'Rio Grande do Sul','initials':'RS'}
state2 = {'uf':'Santa Catarina','initials':'SC'}
brazil.append(state1)
brazil.append(state2)
print(brazil) # [{'uf': 'Rio Grande do Sul', 'initials': 'RS'}, {'uf': 'Santa Catarina', 'initials': 'SC'}]
print(state1) # {'uf': 'Rio Grande do Sul', 'initials': 'RS'}
print(state2) # {'uf': 'Santa Catarina', 'initials': 'SC'}
print(brazil[0]['uf']) # RS


""")
state={}
brazil=[]
for c in range(0,3):
    state['uf'] = str(input("Enter State Name: ")).capitalize()
    state['initials'] = str(input("Enter Initials of State: ")).upper()
    #brazil.append(state[:]) # You can slice dicts as it was on lists
    brazil.append(state.copy()) #You have to copy dicts to lists
print("Printing list (with dicts inside ")
for e in brazil:
    print(e) # Will show dicts 
print("Printing key and values")
for e in brazil:
    for k,v in e.items():
        print(f"Key {k} has value {v}")
print("Printing only Values ")
for e in brazil:
    for v in e.values():
        print(v, end=" ")