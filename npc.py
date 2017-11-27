import time
from random import randint
import game_object
class npc(game_object.game_object):
    name ="John Doe"
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
    enemy=None #target to chace and attack
    is_dead = False
    msg=""
    def __init__(self, x, y, name, is_dead=False):
        self.x = x
        self.y = y
        self.name = name
        self.is_dead = is_dead
    def set_enemy(self, enemy):
        self.enemy = enemy
    def do_action(self):
        self.msg=str(len(self.path))
        if len(self.path) > 1:
            self.move()
        else:
            self.attack(self.enemy)
        self.msg= str(self.hp);
    def move(self):
        self.x, self.y = self.path[0][0], self.path[0][1]
        del self.path[0]
    def attack(self, enemy):
        msg = "attack"
        enemy.taking_damage(randint(-3,3)+self.strength)
        msg = "{0} attacks {1}. ".format(self.name, enemy.name)
        time.sleep(0.1)
        return msg

    def taking_damage(self, damage, aditional_action = None):
        self.hp = self.hp - damage
        msg = "{0} taking {1} damage. ".format(self.name, str(damage))
        if self.hp < 1:
            self.is_dead = True
            self.symbol = "c"
            msg  = msg+"{0} is dead. ".format(self.name)
        return msg
