from ink import Ink
from paper import Paper

class Currency(Ink,Paper):
    bank_name="RBI"

    def __init__(self, colour, density,length,width,thikness,quantity,chemical_resistence,opacity):
        super().__init__(colour, density)
        Paper.__init__(self,length,width,thikness)
        self.quantity=quantity
        self.opacity=opacity
        self.chemical_resistence=chemical_resistence
        self.opacity=opacity

    def info(self):
        self.info1()
        self.info2()
        print(f"Quantity : {self.quantity}\nQuantity : {self.quantity}\nOpacity : {self.opacity}\nChemical Resistence : {self.chemical_resistence}")
        
obj_c=Currency("white",'80%','5m','3m',100,'Yes','Yes','30%')
obj_c.info()