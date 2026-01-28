class Engine_system:
    Company_name="GE Aerospace"

    def __init__(self,engine_type,engine_power):
        self.engine_type=engine_type
        self.engine_power=engine_power
    
    def info1(self):
        print(f"Company Name : {self.Company_name}")
        print(f"Engine Type : {self.engine_type}")
        print(f"Engine Power : {self.engine_power}")



        