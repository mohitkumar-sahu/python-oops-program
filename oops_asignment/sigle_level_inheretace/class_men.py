from class_human import Human
class Men(Human):
    gender="Male"
    
    def __init__(self, first_name, last_name, age, contact_no):
        super().__init__(first_name, last_name, age, contact_no)

    def info2(self):
        self.info()
        print(f"Gender : {self.gender}")

M1=Men("mohit","Sahu","23",9373726312) 
M1.info2()