# 1. positonal Argument
#1.1 non-default
def user_details(name,email,age):
    print(f"Name={name},email={email},age={age}")

user_details("mks","mk183018@gmail.com",23)

# 1.2 defaul argument
def user_details(name,email,age=25):
    print(f"Name={name},email={email},age={age}")

user_details("mks","mk183018@gmail.com")

# 2. Keyword argument
def user_details(name,email,age):
    print(f"Name={name},email={email},age={age}")

user_details(name="mohit",email="mk183018@gmail.com",age=35)

# 3. Arbitary parameter
#3.1 Arbitary variable Parameter

def Sum(*args):
    print(*args)
    return sum(args)

x=Sum(1,2,3,4,5,6,7,8,9)
print(x)

#3.2 Arbitary keyword parameter
def user_details(**kwargs):
    print(kwargs)

user_details(name="mohit",age=20,email="mk183018@gmail.com")

#positonal only argument
def fun(a,b,c,/):
    print(a,b,c)

fun(10,20,30)
#fun(a=10,b=20,c=30)  TypeError: fun() got some positional-only arguments
#passed as keyword arguments: 'a, b, c'

#keywords only Argument
def fun2(*,a,b,c):
    print(a,b,c)

fun2(a=10,b=20,c=30)
# fun2(10,20,30) TypeError: fun2() takes 0 positional arguments but 3 were given

def all_args(a,b,c=10,*d,**e):
    print(a,b,c,d)

all_args(10,b=20,c=30,d=[1,2,3,4],name="mohit",email="mks")