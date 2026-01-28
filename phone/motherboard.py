class Motherboard:
    motherboard_company='Foxcon'

    def __init__(self,processor,RAM,ROM):
        self.processor=processor
        self.RAM=RAM
        self.ROM=ROM

    def Motherboard_info(self):
        print('--------Motherboard Info-----------')
        print(f'Motherboard Company : {self.motherboard_company}\nProcessor : {self.processor}\nRAM : {self.RAM}\nROM : {self.ROM}')