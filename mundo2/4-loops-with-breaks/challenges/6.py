#!/usr/bin/python
print ("""071
Simulate and ATM machine asking how much would like to cash and tell how much of each bill will be delivered (50, 20, 10, 5, 1)
""")

print("="*30)
print("{:^30}".format("Python Bank"))
print("="*30)
cash = int(input("Enter how much would like to cash: "))
total = cash
bill=50
bills=0
while True:
    if total >= bill:
        total-=bill
        bills+=1
    else:
        if bills > 0:
            print("{} bills of ${}".format(bills,bill))
        if bill == 50:
            bill=20
        elif bill == 20:
            bill=10
        elif bill == 10:
            bill=5
        elif bill == 5:
            bill=1
        bills=0
        if total == 0:
            break
print("-"*5,"Have a good day. Take care","-"*5)