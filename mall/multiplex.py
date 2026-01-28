class Multiplex:
    on_floor='5th'
    view='3D'

    def __init__(self,type_of_movie,movie_name):
        self.type_of_movie=type_of_movie
        self.movie_name=movie_name
    
    def multiplex_info(self):
        print(f"On Floor : {self.on_floor}\nType of Movie : {self.type_of_movie}\nMovie Name : {self.movie_name}")
