import game_object
import helper


class gameitem(game_object.game_object):
    def __init__(self, x, y):
        game_object.game_object.__init__(self, x, y)
        self.name = "Unnamed"
        self.drawable = True
        self.symbol = "?"
        self.on_the_ground = True
        self.pickable = True
        self.count = 1
        self.equipable = False

    def pick_up(self):
        self.x, self.y = 0, 0
        self.on_the_ground = False
        self.drawable = False


class coin(gameitem):
    def __init__(self, x, y):
        gameitem.__init__(self, x, y)
        self.name = "Coin"
        self.color_pair = helper.COLOR_YELLOW
        self.symbol = "$"


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


class weapon(gameitem):
    def __init__(self, x=0, y=0, person=None):
        gameitem.__init__(self, x, y)
        self.name = "weapon"
        self.symbol = "/"
        self.damage = 1
        self.equipable = True


class sword(weapon):
    def __init__(self, x=0, y=0, person=None):
        weapon.__init__(self, x, y, person)
        self.damage = 5
        self.symbol = "/"
        self.name = "Sword"
        self.color_pair = helper.COLOR_BLUE


class club(weapon):
    def __init__(self, x=0, y=0, person=None):
        weapon.__init__(self, x, y, person)
        self.damage = 3
        self.symbol = "/"
        self.name = "Club"
        self.color_pair = helper.COLOR_YELLOW
