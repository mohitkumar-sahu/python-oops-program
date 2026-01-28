class Tmt_bars:
    Tmt_bars_company="Tata"

    def __init__(self,width,length,weight):
        self.width=width
        self.length=length
        self.weight=weight

    def bars_info(self):
        print('-------------Bars Info--------------')
        print(f"Bars Company : {self.Tmt_bars_company}\nWidth : {self.width}\nLength : {self.length}\nWeight : {self.weight}")
        