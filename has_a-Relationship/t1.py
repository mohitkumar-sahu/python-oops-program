class Player:
    def __init__(self,name,jersey_no,age,weight):
        self.name=name
        self.jersey_no=jersey_no
        self.age=age
        self.weight=weight
    
    def player_info(self):
        print(f'Name : {self.name}/nJersey_no : {self.jersey_no}/nAge : {self.age}/nWeight : {self.weight}')

class Team:
    def __init__(self,name,jersey_col,player):
        self.name=name
        self.jersey_col=jersey_col
        self.player=player
        
    def team_info(self):
        print(f'Team Name : {self.name}/nJersey Color : {self.jersey_col}')
        self.player.player_info()

obj_P1=Player('virat','10',35,70)
obj1_T1=Team('Team India','Blue',obj_P1)
Team.team_info(obj1_T1)

