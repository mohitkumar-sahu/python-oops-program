val=input("Enter val : ")
values=['a','e','i','o','u','A','E','I','O','U']
if val in values:
    print("vowel")
else:
    print("Not Vowel")

no=int(input("n :  "))
if(100<=no<=999) and not(-99<=no<=99):
    print("3digit")
else:
    print("Not 3 digit")

#Assignment
char=input("Enter char : ")
if char.isalpha():
    print(f"{char} is Alphabet")
elif char.isnumeric():
    print(f"{char} is Numeric")
else:
    print("Special Case ")

# Q.2 
char=input("Enter char : ")
if (char >='A' and char <='Z'):
    print(f"{char} is in Upper Case.")
elif (char >= 'a' and char <='z'):
    print(f"{char} is in Lower Case.")
elif char.isnumeric():
    print(f"{char} is Numeric.")


# Q3
no=int(input("Enter n :"))
if(no>0):
    print(f"{no} is +ve. ")
elif(no<0):
    print(f"{no} is -ve. ")
else:
    print(f"{no} is Zero. ")

#Q4
no=int(input("Enter n :"))
if(-9<=no<=9):
    print("Single digit") 
elif(-99<=no<=99 and not(-9<=no<=9)):
    print("double digit")
elif (-999<=no<=999) and not(-99<=no<=99):
    print("3 digit")

