#!/usr/bin/python

print("""
= = = Repetitions structure = = =
- Lace with control variable 
for control in range(1,10):
    step
catch
for control in range(1,3):
    if coin:
        catch
    step
    jump
step
catch
""")
for i in range(0,3):
    print("Hello Counter {}".format(i))
print("End")
print("#Count backwards")
for i in range(4,0,-1): 
    print(i)
print("End") 
print("#Jumping ")
for i in range(6,0,2): 
    print("Counter {}".format(i))
print("End") 

b = int(input("Enter Start: "))
e = int(input("Enter End: "))
j = int(input("Enter Jump: "))
for i in range(b,e+1,s):
    print(i)
print("Finish")

for i in range(b,e+1,j):
    n = int(input("Enter value: "))
    s += n
print("Finish")