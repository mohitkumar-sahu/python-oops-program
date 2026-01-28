from vehicle import Vehicle

class Truck(Vehicle):
    
    def __init__(self, manufecturar_name, mfg_date, vehical_no, fuel_type, colour,wheels,load_capacity):
        super().__init__(manufecturar_name, mfg_date, vehical_no, fuel_type, colour)
        self.wheels=wheels
        self.load_capacity=load_capacity
    
    def truck_info(self):
        self.vehical_info()
        print(f"No of Wheels : {self.wheels}\nLoad Capacity : {self.load_capacity}")

obj_t=Truck('Tata Moters','11-oct-25','BR-29-1234','Diesal','Black',12,'50 Ton')
obj_t.truck_info()