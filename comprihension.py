# list comprihension
# Get all the even numbers from 0 - 50
# using for loop
l=[]
for i in range(1,51):
    if i%2==0:
        l.append(i)
print(l)
# using list comprihension
l1=[num for num in range(1,51) if num%2==0]
print(l1)

#string that start with 'a' & end with 'y'
l1=[]
options=['any','albony','apple','world','hello','']
for i in options:
    if len(i)>=2:
        if(i[0]=='a' and i[-1]=='y'):
            l1.append(i)
print(l1)

l2=[option for option in options 
    if len(option)>=2 
    if option[0]=='a' and option[-1]=='y']
print(l2)

