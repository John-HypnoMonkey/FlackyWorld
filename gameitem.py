import game_object
class gameitem(game_object.game_object):
    name ="Unnamed"
    x,y=0,0
    drawable =True
    symbol="U"
    on_the_ground = True
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def pick_up(self):
        self.x,self.y=0,0
        self.on_the_ground = False
        self.drawable = False
class coin(gameitem):
    name ="Coin"
    symbol="$"

class heal_potion(gameitem):
    name = "Heal potion"
    symbol = "h"
