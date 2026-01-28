from display import Display
from motherboard import Motherboard
from software import Software

class Phone(Motherboard,Display,Software):
    phone_manufacturer="Apple"
    
    def __init__(self, processor, RAM, ROM,type,size,os,updates,colour,weight,no_of_camera):
        super().__init__(processor, RAM, ROM)
        Display.__init__(self,type,size)
        Software.__init__(self,os,updates)
        self.colour=colour
        self.weight=weight
        self.no_of_camra=no_of_camera

    def phone_info(self):
        print('----------Phone Info----------')
        print(f"Phone Manufacturer : {self.phone_manufacturer}\nColour : {self.colour}\nWeight : {self.weight}\nNo of Camera : {self.no_of_camra}")
        self.software_info()
        self.Motherboard_info()
        self.display_info()
    
obj_p=Phone('A18 pro','8GB','128GB','Amoled','6 inch','ios','Regular','Green','200g',3)
obj_p.phone_info()