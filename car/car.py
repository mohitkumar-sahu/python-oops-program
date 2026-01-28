from engine import Engine
from glass import Glass
from tyre import Tyre

class Car(Engine,Glass,Tyre):
    car_company="BMW"

    def __init__(self, fuel_type, power,engine_type,size,thikness,bullet_proof,type,width,load_capacity,colour,no_of_seat):
        super().__init__(fuel_type, power,engine_type)
        Glass.__init__(self,size,thikness,bullet_proof)
        Tyre.__init__(self,type,width,load_capacity)
        self.colour=colour
        self.no_of_seat=no_of_seat

    def info(self):
        print(f"Car Company : {self.car_company}\nColour : {self.colour}\nNo of Seat : {self.no_of_seat}")
        self.info1()
        self.info2()
        self.info3()

obj_c=Car("petrol",'400HP','Automatic','10M','50mm','Yes','Tubeless','50mm','1000kg','Black',4)
obj_c.info()