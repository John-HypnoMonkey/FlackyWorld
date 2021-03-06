import random
import math
import game_object
import time
import unittest


class TestHelper(unittest.TestCase):
    def test_Distance(self):
        game_obj1 = game_object.GameObject(1, 1)
        game_obj2 = game_object.GameObject(1, 2)
        self.assertEqual(distance(game_obj1, game_obj2), 1)

    def test_GetRandomName(self):
        self.assertIsInstance(getRandomName(), str)


# colors for curses
COLOR_BLACK = 0
COLOR_RED = 1
COLOR_GREEN = 2
COLOR_YELLOW = 3
COLOR_BLUE = 4
COLOR_MAGENTA = 5
COLOR_CYAN = 6
COLOR_WHITE = 7

ALPHABET = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p')


def delay(sleep=0.1):
    time.sleep(sleep)


def distance(game_obj1, game_obj2):
    result = math.sqrt((game_obj1.x - game_obj2.x) ** 2 + (game_obj1.y - game_obj2.y) ** 2)
    return result


def distance2(game_obj1, x2, y2):
    result = math.sqrt((game_obj1.x - x2) ** 2 + (game_obj1.y - y2) ** 2)
    return result


def setRandomPosition(maplist, game_objects):
    for i in range(0, 254):
        rand_y = random.randint(0, 31)
        rand_x = random.randint(0, 63)
        if maplist[rand_y][rand_x] == '-':
            is_position_free = True
            for item in game_objects:
                if rand_x == item.x and rand_y == item.y:
                    is_position_free = False
            if is_position_free is True:
                return rand_x, rand_y


def getRandomName():
    goblins = ['Thraggar', 'Bramath Thok', 'Gaggung', 'Tamok', 'Omouduk',
               "K'ggak", 'Bragak', 'Sumorth', 'Sudang', 'Grumang',
               'Braggok', 'Gramurth', 'Tudong', 'Tumuk', 'Momak',
               'Amaugoth', 'Bramong', 'Taggak Gang', 'Cruduk', "G'dok",
               'Mumak', 'Thodong', 'Saguk', 'Thragak Mok', 'Gramung',
               'Thrudor', 'Mumung', 'Soggurth', 'Maduk Brath', 'Emuugguth',
               'Brogong Mok', 'Emaumoth', 'Togok', 'Tuggong', 'Kragur',
               'Bromurth', 'Thoggak', 'Gradath', "Guggar K'not", "Thrumak",
               "Sadarth", "Tadarth", "Kraguk", "Braguth", "Moduk",
               "Grogok", "Gruggorth", "Aggoumuk", "Mamamng",
               "K'ggung", "Sogok", "Tuggor", "Brugoth Thrar", "Kramarth",
               "Thruguk", "Throdak", "Tugung", "Bramak", "Sugak",
               "Thungung", "Maggong"]
    return goblins[random.randint(0, len(goblins) - 1)]


if __name__ == "__main__":
    unittest.main()
