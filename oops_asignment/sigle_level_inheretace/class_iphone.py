from class_phone import Phone
class Iphone(Phone):
    def __init__(self, brand_name, model_no, colour, battery_capacity,No_of_camera,refresh_rate):
        super().__init__(brand_name, model_no, colour, battery_capacity)
        self.no_of_camera=No_of_camera
        self.refresh_rate=refresh_rate

    def info2(self):
        self.info()
        print(f"No of Camera : {self.no_of_camera}")
        print(f"Refresh Rate : {self.refresh_rate}")

i1=Iphone("Apple","17 Pro","Orange","4000 MAH",3,"120 HZ")
i1.info2()