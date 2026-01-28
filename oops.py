# class Empty:
#     pass

# res=dir(Empty)
# print(len(res)) #-> 27

class Example:
    a=10
    
    def __init__(self,a):
        self.a=a

    def meth(self):
        print("I am Meth")
    
obj=Example(2)
# print(Example.a)
# print(obj.a)

#print(Example.b). AttributeError: type object 'Example' has no attribute 'b'

print(obj.meth())