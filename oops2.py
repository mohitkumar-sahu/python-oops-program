class Student:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age

    def full_details(self):
        return f"{self.name},{self.age}"

class Teacher(Student):
    def __init__(self,name,id,age,sal):
        super().__init__(name,id,age)
        self.salary=sal

    def full_details(self):
        return f"{self.name},{self.age},{self.salary}"
    
    def get_id(self):
        return self.id
    

x=Teacher("Mohit",1,22,20000)
print(x.full_details())
print(x.get_id())
print(Teacher.get_id(x))

