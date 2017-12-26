import game_object
import helper
class gameitem(game_object.game_object):
    def __init__(self, x, y):
        game_object.game_object.__init__(self, x, y)
        self.name ="Unnamed"
        self.drawable =True
        self.symbol="?"
        self.on_the_ground = True
    def pick_up(self):
        self.x,self.y=0,0
        self.on_the_ground = False
        self.drawable = False
class coin(gameitem):
    def __init__(self, x, y):
        gameitem.__init__(self, x, y)
        self.name ="Coin"
        self.color_pair = helper.COLOR_YELLOW
        self.symbol="$"

class heal_potion(gameitem):
    def __init__(self, x, y):
        gameitem.__init__(self, x, y)
        self.name = "Heal potion"
        self.color_pair = helper.COLOR_BLUE
        self.symbol = ","

class cake(gameitem):
    def __init__(self, x, y):
        gameitem.__init__(self, x, y)
        self.name = "Tasty cake"
        self.symbol = "_"
