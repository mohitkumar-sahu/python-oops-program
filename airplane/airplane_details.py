from engine_system import Engine_system
from wing_system import Wing_system

class Airplane_details(Engine_system,Wing_system):

    def __init__(self, engine_type, engine_power,wing_type,wing_span,manufacturar,model_name,length,capacity,fuel_capacity,no_of_engine):
        super().__init__(engine_type, engine_power)
        Wing_system.__init__(self,wing_type,wing_span)
        self.manufacturar=manufacturar
        self.model_name=model_name
        self.length=length
        self.capcity=capacity
        self.fuel_capacity=fuel_capacity
        self.no_of_engine=no_of_engine

    def info(self):
        self.info1()
        self.info2()
        print(f'Manufecturar : {self.manufacturar}\nModel Name : {self.model_name}\nLength : {self.length}\nCapacity : {self.capcity}\nFuel Capacity : {self.length}\nNo of Engine : {self.no_of_engine}')


obj_A=Airplane_details("Gas Turbine Engines","170 HP","Elliptical",'60 M','Boeing','A320',100,70,'200 liter',3)
obj_A.info()