from p1 import Human
class Men(Human):
    gender='Male'
    def __init__(self, name, age, dob, address):
        super().__init__(name, age, dob, address)

    def men_info(self):
        self.human_info()
        print(f'Gender : {self.gender}')
 
obj_m=Men('abc',10,'10-08-15','BTM')
obj_m.men_info()