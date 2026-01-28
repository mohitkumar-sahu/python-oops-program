from genralization import Vehicle

class Car(Vehicle):
    def __init__(self, vechile_no, colour):
        super().__init__(vechile_no, colour)

    def vehicle_info(self):
        print(f'Car no is {self.vechile_no} and colour is {self.colour}')

c1=Car('BR-29-1234','Black')
c1.vehicle_info()