class Game_zone:
    on_floor=3

    def __init__(self,no_of_game,type_of_game):
        self.no_of_game=no_of_game
        self.type_of_game=type_of_game
        
    def game_zone_info(self):
        print(f"On floor : {self.on_floor}\nNo of Game : {self.no_of_game}\nType of Game : {self.type_of_game}" )