from car import Car
from vehicle import Vehicle

class Electric_car(Car,Vehicle):
    def __init__(self,manufecturar_name, mfg_date, vehical_no, fuel_type,colour,no_of_door,price,battery_capacity,auto_pilot):
        super().__init__(manufecturar_name, mfg_date, vehical_no, fuel_type,colour,no_of_door,price)
        Vehicle.__init__(self,manufecturar_name,mfg_date,vehical_no,fuel_type,colour)
        self.battery_capacity=battery_capacity
        self.auto_pilot=auto_pilot

    def electric_car_info(self):
        self.car_info()
        print(f"Battery Capacity : {self.battery_capacity}\nAuto Pilot : {self.auto_pilot}")

