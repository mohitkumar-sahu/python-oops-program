from Hierarichal_inheritance.milk.milk import Milk

class Icecream(Milk):
    brand_name='Amul'

    def __init__(self,milk_type, mfg_date, exp_date,type,flavour,):
        super().__init__(milk_type, mfg_date)
        self.type=type
        self.flavour=flavour
        self.exp_date=exp_date
        
    def icecream_info(self):
        print('-------Ice Cream Info---------')
        print(f'Type : {self.type}\nFlavour : {self.flavour}\n EXP Date : {self.exp_date}')
        self.milk_info()

obj_i=Icecream('Full cream','05-oct-25','08-oct-25','cone','Choclate')
obj_i.icecream_info()
