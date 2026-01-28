#3. Largest of Three Numbers
# Write a Python program that takes three numbers and uses nested if to determine the largest.

a=int(input("Enter first no : "))
b=int(input("Enter second no : "))
c=int(input("Enter third no : "))

if(a>b):
    if(a>c):
        print(f"{a} is largest no ")
    else:
        print(f"{c} is largest no ")
elif(b>a):
    if(b>c):
        print(f"{b} is largest no ")
    else:
        print(f"{c} is largest no")

# 1. Leap Year Checker
# Write a program to check if a year is a leap year:
year = int(input("Enter Year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# Movie Ticket Pricing using match-case

age = int(input("Enter your age: "))

match age:
    case _ if age <= 12:
        price = 100
    case _ if 13 <= age <= 59:
        price = 200
    case _ if age >= 60:
        price = 150
    case _:
        price = "Invalid age"

print(f"Ticket Price: ₹{price}")