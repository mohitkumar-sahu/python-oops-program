class Engine:
    engine_company="xyz"

    def __init__(self,fuel_type,power,engine_type):
        self.fuel_type=fuel_type
        self.power=power
        self.engine_type=engine_type

    def info3(self):
        print(f"Engine Company : {self.engine_company}\nFuel Type : {self.fuel_type}\nPower : {self.power}\nEngine Type : {self.engine_type}")