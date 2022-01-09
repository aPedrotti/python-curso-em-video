#!/usr/bin/python
print ("""070
Read product and prices of a purchase process and asks if want to continue.
Then shows total spent, how much products more expensive than $1000 and what is the name of the cheepest product
""")

cheepest=count=expensives=total=thousands=0
cheepest=99999.00
cheepest_name=" "

print("-="*16)
print(" "*10,"Happy Mall")
print("-="*16)
while True:
    product = str(input("Enter product Name: ")).strip()
    price = float(input("Enter product's price: $"))
    count+=1
    if price >=1000:
        expensives+=1
    if count == 1 or price < cheepest:
        cheepest_name=product
        cheepest=price
    total+=price
    cont=" "
    while cont not in "YN":
        cont = str(input("Would like to continue? [Y/N] ")).strip().upper()[0]
    print("-"*32)
    if cont == "N":
        break
print("{:^32}".format("CHECKOUT"))
print("""Total: ${:.2f}
You bought {} products more expensive than 1000
The Cheepest product was {}
""".format(total,expensives,cheepest_name))