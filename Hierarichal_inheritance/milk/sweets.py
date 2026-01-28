from Hierarichal_inheritance.milk.milk import Milk

class Sweets(Milk):
    shop_name="Haldiram"
    branch='BTM'

    def __init__(self, milk_type, mfg_date,sweet_name,exp_date,price):
        super().__init__(milk_type, mfg_date)
        self.sweet_name=sweet_name
        self.exp_date=exp_date
        self.price=price

    def sweets_info(self):
        print('----------Sweets Info-----------')
        print(f"Shop Name : {self.shop_name}\nBranch : {self.branch}")
        print(f"Sweet Name : {self.sweet_name}\nEXP Date : {self.exp_date}\nPrice : {self.price}")
        self.milk_info()


obj_s=Sweets('full Cream','07-10-25','Gulab Jamun','15-10-25','300rs per/kg')

obj_s.sweets_info()