from store import Store
from multiplex import Multiplex
from game_zone import Game_zone

class Mall(Store,Multiplex,Game_zone):
    mall_name='Vega City'
    address='BTM Layout'

    def __init__(self, store_type, no_of_items, no_of_staff,type_of_movie,movie_name,no_of_game,type_of_game,):
        super().__init__(store_type, no_of_items, no_of_staff)
        Multiplex.__init__(self,type_of_movie,movie_name)
        Game_zone.__init__(self,no_of_game,type_of_game)

    def mall_info(self):
        print('-----------Mall Info-----------')
        print(f"Mall Name : {self.mall_name}\nAddress : {self.address}\n")
        self.store_info()
        self.multiplex_info()
        self.game_zone_info()

obj_m=Mall('Clothing',500,10,'Action','KGF',50,'Racing')
obj_m.mall_info()
