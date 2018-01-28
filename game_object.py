import helper


class game_object:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.drawable = False
        self.symbol = "?"
        self.color_pair = helper.COLOR_WHITE
