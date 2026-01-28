class Phone:
    def __init__(self,brand_name,model_no,colour,battery_capacity):
        self.brand_name=brand_name
        self.model_no=model_no
        self.colour=colour
        self.battery_capacity=battery_capacity

    def info(self):
        print(f"Brand Name : {self.brand_name}\nModel_No : {self.model_no}\nColour : {self.colour}\nBattery Capacity : {self.battery_capacity}")
    