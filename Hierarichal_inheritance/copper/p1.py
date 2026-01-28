class Copper:
    country_of_origin='India'

    def __init__(self,grade):
        self.grade=grade
    
    def copper_info(self):
        print('--------Copper Info----------')
        print(f"Country of Origin : {self.country_of_origin}\nGrade : {self.grade}")