class Player:
    def __init__(self,name,age,height,player_no):
        self.name=name
        self.age=age
        self.height=height
        self.player_no=player_no
    
    def player_info(self):
        print('-------------Player Info--------------')
        print(f"Name : {self.name}\nAge : {self.age}\nHeight : {self.height}\nPlayer_no : {self.player_no}")


class Team:
    def __init__(self,player,jersey_colour,country,coach,captain):
        self.player=player
        self.jersey_colour=jersey_colour
        self.country=country
        self.coach=coach
        self.captain=captain

    def team_info(self):
        print('--------------Team Info--------------')
        print(f'Country : {self.country}\nJersey Colour : {self.jersey_colour}\nCoach : {self.coach}\nCaptain : {self.captain}')
        self.player.player_info()

obj_p=Player('Lional Messi','30',5.8,10)
obj_t=Team(obj_p,'pink','Argentina','abc','xyz')
obj_t.team_info()