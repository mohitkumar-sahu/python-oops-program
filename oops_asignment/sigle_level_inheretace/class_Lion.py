from class_Animal import Animal

class Lion(Animal):
    no_of_foot=4
    diet = "Cornivore"
    def __init__(self,name, age, habitat, weight):
        super().__init__(name, age, habitat, weight)
        
    def info2(self):
        self._info()
        print(f"No of Foot : {self.no_of_foot}\nDiet:{self.diet}")

l1=Lion("mks",23,"forest",55)
l1.info2()

    