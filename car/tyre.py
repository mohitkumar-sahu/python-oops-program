class Tyre:
    tyre_company="MRF"

    def __init__(self,type,width,load_capacity):
        self.type=type
        self.width=width
        self.load_capcity=load_capacity

    def info1(self):
        print(f'Tyre Company : {self.tyre_company}\nTyre Type : {self.type}\nWidth : {self.width}\nLoad Capacity : {self.load_capcity}')
        