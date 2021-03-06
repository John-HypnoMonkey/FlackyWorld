# -*- coding: utf-8 -*-
from random import randint
import game_object
import gameitem
import game_log
import inventory


class Player(game_object.GameObject):

    def __init__(self, x, y):
        game_object.GameObject.__init__(self, x, y)
        self.equipment = {'HEAD': '', 'NECK': '', 'L.ARM': '', 'R.ARM': '',
                          'L.HAND': '', 'R.HAND': '', 'TORSO': '', 'LEGS': ''}
        self.name = "Hero"
        self.hp = 200
        self.maxhp = 200
        self.level = 1
        self.exp = 0
        self.strength = 8
        self.agility = 5
        self.damage = 0
        self.coins = 0
        self.chance_to_evade = 0
        self.player_action_cost = 0
        self.is_dead = False
        self.message = ""
        self.symbol = "@"
        self.next_action_func = None
        self.next_action_args = None

    def attack(self, enemy):
        game_log.GameLog.addMessage("You punch {0}".format(enemy.name))
        enemy.takingDamage(randint(-3, 3) + self.strength)

    def takingDamage(self, damage, aditional_action=None):
        self.hp = self.hp - damage
        if self.hp < 1:
            self.is_dead = True
#    def heal(self, add_hp):
#        self.hp += add_hp
#        if self.hp > self.maxhp:
#            self.hp = self.maxhp
#        game_log.game_log.add_message("You fill yourself much better")

    def move(self, new_x, new_y, maplist, items, npcs):
        if self.canMove(new_x, new_y, maplist, npcs):
            for val in items:
                if val.x == new_x and val.y == new_y:
                    val.on_the_ground = False
                    val.x, val.y = -1, -1
                    if val.__class__ == gameitem.Coin:
                        self.coins += 1
                    else:
                        inventory.Inventory.addItem(val)
                        game_log.GameLog.addMessage("You pick up a {0}".format(val.name))
            self.x = new_x
            self.y = new_y
        else:
            pass

    def canMove(self, x, y, maplist, npcs):

        for val in npcs:
            if val.x == x and val.y == y and val.is_dead is False:
                self.attack(val)
                return False
                pass

        if maplist[y][x] == "#":
            return False
        else:
            return True

    def setNextAction(self, func, args):
        self.next_action_func = func
        self.next_action_args = args

    def doAction(self):
        if self.next_action_func is not None:
            self.next_action_func(*self.next_action_args)
            self.next_action_args = None
            self.next_action_func = None
