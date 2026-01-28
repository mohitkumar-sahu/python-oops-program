from p1 import Human

class Women(Human):
    gender='Female'

    def __init__(self, name, age, dob, address):
        super().__init__(name, age, dob, address)

    def women_info(self):
        self.human_info()
        print(f"Gender : {self.gender}")
obj_w=Women('xyz',20,'05-05-2005','Bengaluru')
obj_w.women_info()
