class Vehicle:
    def __init__(self,manufecturar_name,mfg_date,vehical_no,fuel_type,colour):
        self.manufecturar_name=manufecturar_name
        self.mfg_date=mfg_date
        self.vehical_no=vehical_no
        self.fuel_type=fuel_type
        self.colour=colour
        
    def vehical_info(self):
        print('---------Vehical Info----------')
        print(f'Manufecturar Name : {self.manufecturar_name}\nMFG Date : {self.mfg_date}\nVehical No : {self.vehical_no}\nFuel Type : {self.fuel_type}\nColour : {self.colour}')


    
