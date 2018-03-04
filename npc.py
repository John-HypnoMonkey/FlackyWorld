import time
from random import randint
import game_object
import helper
import game_log


class npc(game_object.GameObject):

    def __init__(self, x, y, name="", is_dead=False):
        game_object.GameObject.__init__(self, x, y)
        self.__name = name
        self.hp = 10
        self.maxhp = 10
        self.saw_player = True
        # list of path from the npc to enemy
        self.path = []
        self.strength = 5
        self.agility = 5
        self.damage = 0
        # symbol that will represent the npc on a map
        self.symbol = "g"
        self.chance_to_evade = 0
        self.target = None
        self.what_to_do_with_target = ("goto", "runaway", "be_on_distance")
        self.is_dead = False
        self.drawable = True

        self.race = ""
        self.job = ""
        self.x = x
        self.y = y
        self.is_dead = is_dead

    @property
    def name(self):
        if self.__name != "":
            if self.job != "":
                return "{0}, {1} {2}".format(self.__name, self.job, self.race)
            else:
                return "{0}, {1}".format(self.__name, self.race)
        else:
            return "{0}".format(self.race)

    def setEnemy(self, enemy):
        self.target = enemy

    def doAction(self):
        if len(self.path) > 1:
            self.move()
        else:
            if len(self.path) > 0:
                self.attack(self.target)

    def move(self):
        if len(self.path) > 0:
            self.x, self.y = self.path[0][0], self.path[0][1]
            del self.path[0]

    def attack(self, enemy):
        enemy.takingDamage(randint(-3, 3) + self.strength)
        game_log.GameLog.addMessage("{0} attacks {1}. ".format(self.name, enemy.name))
        time.sleep(0.1)

    def takingDamage(self, damage, aditional_action=None):
        self.hp = self.hp - damage
        game_log.GameLog.addMessage("{0} is taking {1} damage. ".format(self.name, str(damage)))
        if self.hp < 1:
            self.is_dead = True
            self.drawable = False
            self.symbol = "c"
            game_log.GameLog.addMessage("{0} is dead. ".format(self.name))


class Goblin(npc):
    def __init__(self, x, y, name="", is_dead=False):
        npc.__init__(self, x, y, name, is_dead)
        self.color_pair = helper.COLOR_RED

        self.race = "goblin"


class GoblinCapitan(Goblin):
    def __init__(self, x, y, name="", is_dead=False):
        Goblin.__init__(self, x, y, name, is_dead)
        self.color_pair = helper.COLOR_CYAN
        self.job = "capitan"
        self.hp = randint(12, 30)
        self.strength = randint(8, 10)
