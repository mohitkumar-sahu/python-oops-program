from cement import Cement
from tmt_bars import Tmt_bars

class Apartment(Cement,Tmt_bars):
    Apartment_company="DLF"

    def __init__(self, mfg_date, exp_date,width,length,weight,no_of_room,floor,):
        super().__init__(mfg_date, exp_date)
        Tmt_bars.__init__(self,width,length,weight)
        self.no_of_room=no_of_room
        self.floor=floor

    def aprt_info(self):
        print('-------------Apartment Info--------------')
        print(f'Apartemnt Company : {self.Apartment_company}\nNo of Room : {self.no_of_room}\nFloor : {self.floor}')
        self.bars_info()
        self.cement_info()

obj_a=Apartment('10-Sep-2025','10-Jan-2026','30mm','20m','30kg',4,20)
obj_a.aprt_info()
