
class Battery:
    var=None
    def __init__(self,battery_capacity,battery_meterial):
        if Battery.var==None:
            Battery.var=self
            self.battery_capacity=battery_capacity
            self.battery_meterial=battery_meterial
        else:
            raise Exception('This is singalton Class')
            
    def battery_info(self):
        print('----------Battery Info-----------')
        print(f"Battery Capacity : {self.battery_capacity}\nBattery Material : {self.battery_meterial}")

class Phone:
    b1=Battery('4000 MAH','Li-polymer')
    b2=Battery('4000 MAH','Li-polymer')
    def __init__(self,brand_name,no_of_camra,display_size,os):
        self.brand_name=brand_name
        self.no_of_camera=no_of_camra
        self.display_size=display_size
        self.os=os
    def phone_info(self):
        print(f'Brand Name : {self.brand_name}\n No of Camera : {self.no_of_camera}\nDisplay Size : {self.display_size}\nOperating System : {self.os}')
        Phone.b1.battery_info()

obj_p=Phone('Apple',3,'6 inch','ios')
obj_p.phone_info()