from oops_asignment.parent_class import Appliance

class Washing_machine(Appliance):

    def __init__(self,brand,model,colour,energy_rating,power,loading_position,drum_oriantation):
        # super().__init__(brand,model,colour,energy_rating,power)
        # self.loading_position=loading_position
        # self.drum_oriantation=drum_oriantation
        Appliance.__init__(self,brand,model,colour,energy_rating,power)
        self.loading_position=loading_position
        self.drum_oriantation=drum_oriantation

    def details(self):
        print(f"Brand : {self.brand}\nModel : {self.model}\nColour : {self.colour}\nEnergy Rating : {self.energy_rating}\nPower : {self.power}\nLoading Position :{self.loading_position}")

w1=Washing_machine("LG","abcd","Black",4,"240V","Front Load","Vertical")
w1.details()