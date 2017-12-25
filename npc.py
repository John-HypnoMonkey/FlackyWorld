import time
from random import randint
import game_object
import helper
import game_log
class npc(game_object.game_object):
    name ="monster"

    x = 0
    y = 0
    hp = 10
    maxhp = 10
    saw_player=True
    path = [] #list of path from the npc to enemy
    strength = 5
    agility = 5
    damage = 0
    symbol = "g" #symbol that will represent the npc on a map
    chance_to_evade = 0
    target=None #target to chase and attack
    what_to_do_with_target=("goto","runaway","be_on_distance")
    is_dead = False
    drawable= True
    msg=""
    def __init__(self, x, y, name="", is_dead=False):
        self.x = x
        self.y = y
        if name != "":
            self.name = '{0}, {1}'.format(name, self.name)
        self.is_dead = is_dead
    def set_enemy(self, enemy):
        self.target = enemy
    def do_action(self):
        if len(self.path)>1:
            self.move()
        else:
            if len(self.path)>0:
                self.attack(self.target)

    def move(self):
        if len(self.path)>0:
            self.x, self.y = self.path[0][0], self.path[0][1]
            del self.path[0]
    def attack(self, enemy):
        enemy.taking_damage(randint(-3,3)+self.strength)
        game_log.game_log.add_message("{0} attacks {1}. ".format(self.name, enemy.name))
        time.sleep(0.1)

    def taking_damage(self, damage, aditional_action = None):
        self.hp = self.hp - damage
        game_log.game_log.add_message("{0} taking {1} damage. ".format(self.name, str(damage)))
        if self.hp < 1:
            self.is_dead = True
            self.drawable = False
            self.symbol = "c"
            game_log.game_log.add_message("{0} is dead. ".format(self.name))


class goblin(npc):
    name = "goblin"

class goblin_capitan(goblin):
    name = "goblin capitan"
