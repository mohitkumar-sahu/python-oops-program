from class_cloths import Cloths

class Tshirt(Cloths):

    def __init__(self, brand, colour, febric, size, price):
        super().__init__(brand, colour, febric)
        self.size=size
        self.price=price

    def info2(self):
        self.info()
        print(f"Size : {self.size}")
        print(f"Price : {self.price}")

t1=Tshirt("H&M","Purple","cotton Blend","M",1000)
t1.info2()