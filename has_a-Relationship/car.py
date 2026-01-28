class Engine:
    var=None
    def __init__(self,engine_no,mfg_date,no_of_cylinder,fuel_type):
        if Engine.var==None:
            Engine.var=self
            self.engine_no=engine_no
            self.mfg_date=mfg_date
            self.no_of_cylinder=no_of_cylinder
            self.fuel_type=fuel_type
        else:
            raise Exception("This is Singal Ton Class")
    def engine_info(self):
        print('---------Engine Info----------')
        print(f"Engine No : {self.engine_no}\nMFG Date : {self.mfg_date}\nNo Of Cylinder : {self.no_of_cylinder}\nFuel Type : {self.fuel_type}")

class Car:
    # e1=Engine('abc1234','14-oct-25',4,'Diesel')
    def __init__(self,brand_name,car_no,no_of_door,price):
        self.brand_name=brand_name
        self.car_no=car_no
        self.no_of_door=no_of_door
        self.price=price
        self.e2=Engine('abc1234','14-oct-25',4,'Diesel')
        self.e3=Engine('abc1234','14-oct-25',4,'Diesel')
        #self.e3=Engine(engine_no,mfg_date,no_of_cylinder,fuel_type)
    
    def car_info(self):
        print('--------Car Info-----------')
        print(f"Brand Name : {self.brand_name}\nCar No : {self.car_no}\nNo of Door : {self.no_of_door}\nPrice : {self.price}")
        self.e2.engine_info()
        # self.e3.engine_info()

c1=Car('Toyota','BR 29 0001',4,'40L')
c1.car_info()
