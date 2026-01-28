from vehicle import Vehicle

class Bike(Vehicle):
    no_of_wheels=2
    def __init__(self, manufecturar_name, mfg_date, vehical_no, fuel_type, colour,tank_capacity):
        super().__init__(manufecturar_name, mfg_date, vehical_no, fuel_type, colour)
        self.tank_capacity=tank_capacity

    def bike_info(self):
        self.vehical_info()
        print(f"No of Wheels : {self.no_of_wheels}\nTank Capacity : {self.tank_capacity}")

obj_b=Bike('Yamaha','11-oct-25','abc123','petrol','Black','15L')
obj_b.bike_info()