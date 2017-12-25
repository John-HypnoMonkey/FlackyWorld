import random
import math
import game_object
import time
import unittest

class test_helper(unittest.TestCase):
    def test_distance(self):
        game_obj1 = game_object.game_object(1,1)
        game_obj2 = game_object.game_object(1,2)
        self.assertEqual(distance(game_obj1,game_obj2), 1)


def delay(sleep = 0.1):
    time.sleep(sleep)


def distance(game_obj1, game_obj2):
    result = math.sqrt( (game_obj1.x - game_obj2.x)**2 + (game_obj1.y - game_obj2.y)**2)
    return result
def distance2(game_obj1, x2, y2):
    result = math.sqrt( (game_obj1.x - x2)**2 + (game_obj1.y - y2)**2)
    return result
def set_random_position(maplist, game_objects):
    for i in range(0, 254):
        rand_y = random.randint(0,31)
        rand_x = random.randint(0,63)
        if maplist[rand_y][rand_x] == '-':
            is_position_free = True
            for item in game_objects:
                if rand_x == item.x and rand_y == item.y:
                    is_position_free = False
            if is_position_free == True:
                return rand_x, rand_y



if __name__ == "__main__":
    unittest.main()
