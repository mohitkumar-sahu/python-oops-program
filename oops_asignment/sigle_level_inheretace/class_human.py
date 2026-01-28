class Human:
    scientific_name="Homo sapiens"

    def __init__(self,first_name,last_name,age,contact_no):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.contact_no=contact_no

    def info(self):
        print(f"First Name : {self.first_name}\nLast Name={self.last_name}\nAge :{self.age}\nContact_No={self.contact_no}")

