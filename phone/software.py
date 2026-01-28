class Software:
    software_company='Apple'

    def __init__(self,os,updates):
        self.os=os
        self.updates=updates

    def software_info(self):
        print('-------------Software Info--------------')
        print(f"Software Company : {self.software_company}\nOperating System : {self.os}\nUpdates : {self.updates}\n")