#!/usr/bin/python
print ("""
Cost of a product based on form of payment
money/check - 10% off
card 1x     - 5% off
card 2x     - normal
card >=3x   - 20% fee
""")

price = float(input("Enter the price of product (use DOT as separator): "))
print("""[1] money/check 10% off
[2] card 1x     - 5% off
[3] card 2x     - normal
[4] card >=3x   - 20% fee""")
payment = int(input("Choose your Payment Method: "))
print("Your product will be: ".format(end=''))
if payment == 1:
    print("${:.2f}".format(price*0.9))
elif payment == 2:
    print("${:.2f}".format(price*0.95))
elif payment == 3:
    print("${:.2f}".format(price))
elif payment == 4:
    print("${:.2f}".format(price*1.2))
else:
    print("Unknown payment method! ")
