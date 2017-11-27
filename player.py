# -*- coding: utf-8 -*-
from random import randint
import game_object
import gameitem
class player(game_object.game_object):

    name ="Hero"
    x = 0
    y = 0
    hp = 20
    maxhp = 20
    level = 1
    exp = 0
    strength = 8
    agility = 5
    damage = 0
    coins = 0
    chance_to_evade = 0
    player_action_cost = 0
    is_dead = False
    message =""
    symbol = "@"
    next_action_func = None
    next_action_args = None
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def attack(self, enemy):
        enemy.taking_damage(randint(-3,3)+self.strength)
    def taking_damage(self, damage, aditional_action = None):
        self.hp = self.hp - damage
        if self.hp < 1:
            self.is_dead = True
    def heal(self, add_hp):
        self.hp += add_hp
        if self.hp > self.maxhp:
            self.hp = self.maxhp
    def move(self, new_x, new_y, maplist, items, npcs):
        if self.canmove(new_x, new_y, maplist, npcs):
            for val in items:
                if val.x == new_x and val.y == new_y:
                    val.on_the_ground = False
                    val.x, val.y = -1, -1
                    if val.__class__ == gameitem.coin:
                        self.coins +=1
                    elif val.__class__ == gameitem.heal_potion:
                        self.heal(10)
            self.x=new_x
            self.y=new_y
        else:
            pass



    def canmove(self, x, y, maplist, npcs):

        for val in npcs:
            if val.x == x and val.y == y and val.is_dead == False:
                self.attack(val)
                return False
                pass

        if maplist[y][x] == "#":
            return False
        else:
            return True
    def set_next_action(self,func, args):
        self.next_action_func = func
        self.next_action_args = args
    def do_action(self):
        if self.next_action_func != None:
           self.next_action_func( *self.next_action_args)
           self.next_action_args = None
           self.next_action_func = None
