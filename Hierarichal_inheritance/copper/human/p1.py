class Human:

    def __init__(self,name,age,dob,address):
        self.name=name
        self.age=age
        self.dob=dob
        self.address=address
    
    def human_info(self):
        print("---------Info----------")
        print(f'Name : {self.name}\nAge : {self.age}\nDate of Birth : {self.dob}\nAddress : {self.address}')

