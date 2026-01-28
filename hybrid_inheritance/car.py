from vehicle import Vehicle

class Car(Vehicle):
    no_of_wheels=4

    def __init__(self, manufecturar_name, mfg_date, vehical_no, fuel_type,colour,no_of_door,price):
        super().__init__(manufecturar_name, mfg_date, vehical_no, fuel_type,colour)
        self.no_of_door=no_of_door
        self.price=price

    def car_info(self):
        self.vehical_info()
        print(f'No of Wheels : {self.no_of_wheels}')
        print(f"No of Door : {self.no_of_door}\nPrice : {self.price}")