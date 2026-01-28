from p1 import Copper

class Cookware(Copper):
    company_name="abc"
    gst_no='abc12345'

    def __init__(self, grade,type,weight,price):
        super().__init__(grade)
        self.type=type
        self.weight=weight
        self.price=price

    def cookware_info(self):
        print('--------Cookware Info----------')
        print(f'Company Name : {self.company_name}\nGST NO : {self.gst_no}\nType : {self.type}\nWeight : {self.weight}\nPrice : {self.price}')
        self.copper_info()

obj_c=Cookware('A','Glass','50g',50)
obj_c.cookware_info()