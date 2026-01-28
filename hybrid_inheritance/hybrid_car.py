from car import Car
from electric_car import Electric_car
from vehicle import Vehicle

class Hybrid_car(Electric_car,Car,Vehicle):

    def __init__(self, manufecturar_name, mfg_date, vehical_no, fuel_type, colour, no_of_door, price, battery_capacity, auto_pilot,mileage):
        super().__init__(manufecturar_name, mfg_date, vehical_no, fuel_type, colour, no_of_door, price, battery_capacity, auto_pilot)
        Vehicle.__init__(self,manufecturar_name,mfg_date,vehical_no,fuel_type,colour)
        Car.__init__(self,manufecturar_name, mfg_date, vehical_no, fuel_type,colour,no_of_door,price)
        self.mileage=mileage

    def Hybrid_car_info(self):
        self.electric_car_info()
        print(f"Mileage : {self.mileage}")

obj_h=Hybrid_car('Tata Moters','11-oct-25','ABC1234',['Petrol','CNG'],'Black',4,'30L','80KW','Yes','300KM')
obj_h.Hybrid_car_info()

