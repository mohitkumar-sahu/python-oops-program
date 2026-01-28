class Ink:
    ink_company='ABC'
    manufactur_country='India'

    def __init__(self,colour,density):
        self.colour=colour
        self.density=density
    
    def info2(self):
        print(f"Ink Company : {self.ink_company}\nManufactur Country : {self.manufactur_country}\nColour : {self.colour},Density :{self.density}")
        