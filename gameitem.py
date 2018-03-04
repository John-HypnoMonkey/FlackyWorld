import game_object
import helper


class GameItem(game_object.GameObject):
    def __init__(self, x, y):
        game_object.GameObject.__init__(self, x, y)
        self.name = "Unnamed"
        self.drawable = True
        self.symbol = "?"
        self.on_the_ground = True
        self.pickable = True
        self.count = 1
        self.equipable = False

    def pickUp(self):
        self.x, self.y = 0, 0
        self.on_the_ground = False
        self.drawable = False


class Coin(GameItem):
    def __init__(self, x, y):
        GameItem.__init__(self, x, y)
        self.name = "Coin"
        self.color_pair = helper.COLOR_YELLOW
        self.symbol = "$"


class HealPotion(GameItem):
    def __init__(self, x, y):
        GameItem.__init__(self, x, y)
        self.name = "Heal potion"
        self.color_pair = helper.COLOR_BLUE
        self.symbol = ","


class Cake(GameItem):
    def __init__(self, x, y):
        GameItem.__init__(self, x, y)
        self.name = "Tasty cake"
        self.symbol = "_"


class Weapon(GameItem):
    def __init__(self, x=0, y=0, person=None):
        GameItem.__init__(self, x, y)
        self.name = "weapon"
        self.symbol = "/"
        self.damage = 1
        self.equipable = True


class Sword(Weapon):
    def __init__(self, x=0, y=0, person=None):
        Weapon.__init__(self, x, y, person)
        self.damage = 5
        self.symbol = "/"
        self.name = "Sword"
        self.color_pair = helper.COLOR_BLUE


class Club(Weapon):
    def __init__(self, x=0, y=0, person=None):
        Weapon.__init__(self, x, y, person)
        self.damage = 3
        self.symbol = "/"
        self.name = "Club"
        self.color_pair = helper.COLOR_YELLOW
