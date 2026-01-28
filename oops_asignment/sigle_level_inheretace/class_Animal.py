class Animal:
    no_of_foot=4
    def __init__(self,name,age,habitat,weight):
        self.name=name
        self.age=age
        self.habitat=habitat
        self.weight=weight

    def _info(self):
        print(f"-------Animal Details-------")
        print(f"Name : {self.name}\nAge : {self.age}\nHabitat : {self.habitat}\nWeight : {self.weight}")

obj_a=Animal('lion',20,'Forest',80)
obj_a._info()