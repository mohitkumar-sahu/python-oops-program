class Employee:
    def __init__(self,name=None,age=None):
        self.__name=name
        self.__age=age

    @property
    def get_name(self):
        return self.__name
    
    @property
    def get_age(self):
        return self.__age
    
    @get_age.setter
    def set_age(self,age):
        self.age=age
        
    @get_name.setter
    def set_name(self,name):
        self.name=name

e1=Employee("Mohit",24)
print(e1.get_name)
print(e1.get_age)
