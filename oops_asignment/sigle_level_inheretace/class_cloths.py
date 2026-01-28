class Cloths:
    store_name="Mall"

    def __init__(self,brand,colour,febric):
        self.brand=brand
        self.colour=colour
        self.febric=febric

    def info(self):
        print(f"Store Name : {self.store_name}")
        print(f"Brand Name : {self.brand}")
        print(f"Colour : {self.colour}")
        print(f"Febric : {self.febric}")