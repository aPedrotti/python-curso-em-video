#!/usr/bin/python
print ("""067
Show times table acording user's number entry. Stops when types negative number
""")

print("="*40)
print(" "*15,"TIMES TABLE")
print("="*40)
while True:
    n = int(input("Enter a number to get its times table: "))
    if n < 0:
        break
    print("-"*10)
    for i in range(1,11):
        print("{} x {} = {}".format(n,i,n*i))
    print("-"*10)
print("Finished! Have a good day ! ")