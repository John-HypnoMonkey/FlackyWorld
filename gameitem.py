class gameitem:
    name ="Unnamed"
    x,y=0,0
    symbol="U"
    on_the_ground = True
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def pick_up(self):
        self.x,self.y=0,0
        self.on_the_ground = False

class coin(gameitem):
    name ="Coin"
    symbol="$"

