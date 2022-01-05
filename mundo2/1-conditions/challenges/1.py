#!/usr/bin/python
print ("""
Calculate from if a loan can be provided based on House's value, Salary of the person and how much years he/she is going to take to pay
The monthly amount to be payed cannot be higher than 30%\ of his/her salary. Otherwise it will be denied.
""")

house = float(input("Enter the price of the house: $"))
salary = float(input("Enter your Salary: $"))
years = int(input("Enter how much years are you going to take to pay off: "))

salary_capacity = salary*0.3
morgage = house / (years * 12)

if morgage > salary_capacity:
    print(" Loan \033[30;41mDenied\033[m. Your salary payment capacity is {:.2f} and morage would be {:.2f} ".format(salary_capacity,morgage))
else:
    print(" Loan \033[30;42mAutorized\033[m. Your salary payment capacity is {:.2f} and morage would be {:.2f} ".format(salary_capacity,morgage))
