import curses
import time
import rogmap
import player
import gameitem
import npc
import search_way
import copy
import random
import game_object
import math
import raycast
import helper
import game_log
import menu
import inventory
import os
class GameMode:
    game,menu = range(2)

def draw_inventory(stdscr,x,y):
    x2 = x+ 5
    y2 = y+ 3
    i = 0
    alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']
    for item in inventory.inventory.items:
        result = "{0}) {1}".format(alphabet[i],item.name)
        if item.count > 1:
            result= "{0} ({1})".format(result, item.count)
        stdscr.addstr(y2+i, x2, result)
        i+=1
def draw_log(stdscr,x,y):
    x2 = x+ 5
    y2 = y + 3
    log = game_log.game_log.get_log()
    i = 0
    for item in log[::-1]:
        stdscr.addstr(y2+i, x2, item)
        i+=1
        if i > 25:
            break
def draw_help(stdscr,x,y):
    x2 = x+5
    y2 = y+3
    helpinfo= \
"""Welcome to my roguelike.
Use wasd to move.
'@' is your character
'g' are your enemies
',', '$' are items what you can pickup
Press 'i' to open inventory, and 'l' to open log
Press 'q' to exit the game
"""
    i = 0
    for item in helpinfo.split('\n'):
        stdscr.addstr(y2+i, x2, item)
        i+=1
def draw_exit_message(stdscr,x,y):
    x2 = x+5
    y2 = y+2
    message = "Do you realy want to exit? y/n"
    stdscr.addstr(y2, x2, message)

def curses_main(args):
    def close_active_menu():
        nonlocal active_menu, game_mode
        if active_menu != None:
            active_menu.is_visible=False
            active_menu=None
        game_mode=GameMode.game
    def set_active_menu(item_menu):
        nonlocal active_menu, game_mode
        item_menu.is_visible=True
        active_menu=item_menu
        game_mode=GameMode.menu


    #setting up curses
    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(True)
    curses.noecho()
    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(0, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)
    #os.environ.setdefault('ESCDELAY', '20')
    curses.curs_set(0)
    #inits some important values

    #inits menu windows
    menus = {}
    menus['log']=menu.pop_up_window(stdscr,name="log", draw_func=draw_log)
    menus['inventory']=menu.pop_up_window(stdscr,name="inventory", draw_func=draw_inventory)
    menus['help']=menu.pop_up_window(stdscr,name="help",draw_func=draw_help)
    menus['exit']=menu.pop_up_window(stdscr,25,15,40,4,"exit the game", draw_exit_message)
    active_menu = None
    #set game mode
    game_mode=GameMode.game
    rogmap1 = rogmap.rogmap()
    rogmap1.init()
    game_objects = []
    player1 = player.player(1,1)
    game_objects.append(player1)
    npcs = []
    gameitems = []
    game_log.game_log.add_message("Press '?' for help")
    search_way1 = search_way.search_way()
    #size of the map
    width = 63
    height = 31

    maplist = rogmap1.getmaplist()
    #find some place for our hero
    player1.x, player1.y = helper.set_random_position(maplist, game_objects)
    #add some coins
    random_count = random.randint(10,20)
    for i in range(0, random_count):
        x,y = helper.set_random_position(maplist, game_objects)
        gameitems.append(gameitem.coin(x,y))
        game_objects.append(gameitems[-1])
    #add heal potions
    random_count = random.randint(4,6)
    for i in range(0, random_count):
        x,y = helper.set_random_position(maplist, game_objects)
        gameitems.append(gameitem.heal_potion(x,y))
        game_objects.append(gameitems[-1])
    #add cakes :3
    random_cout = random.randint(4,10)
    for i in range(0,random_count):
        x,y = helper.set_random_position(maplist, game_objects)
        gameitems.append(gameitem.cake(x,y))
        game_objects.append(gameitems[-1])
    #add some enemies
    random_count = random.randint(5,9)
    for i in range(0,random_count):
        x,y = helper.set_random_position(maplist, game_objects)
        npcs.append(npc.goblin(x,y,helper.get_random_name()))
        game_objects.append(npcs[-1])
    random_count = random.randint(1,3)
    for i in range(0,random_count):
        x,y = helper.set_random_position(maplist, game_objects)
        npcs.append(npc.goblin_capitan(x,y, helper.get_random_name()))
        game_objects.append(npcs[-1])
    #all enemies will chase player
    for val in npcs:
        val.set_enemy(player1)
    #main loop
    while True:
        #drawing a map
        raycast.raycast(stdscr, maplist, game_objects, player1.x, player1.y)

        if player1.is_dead == True:
            game_log.game_log.add_message("You are dead. Press 'q' to exit")
        else:
            #draws main character
            stdscr.addstr(player1.y,player1.x,"@",curses.color_pair(helper.COLOR_YELLOW))
        #adding HUD
        stdscr.addstr(32, 2, "Name: {0} level: {1} HP: {2}/{3} Coins: {4}".format(
        player1.name, player1.level, player1.hp, player1.maxhp, player1.coins))
       # stdscr.addstr(38, 2, global_msg)

        #show message log
        game_log.game_log.show_log(stdscr)

        for key in menus:
            menus[key].draw()
        #listen to keyinput
        c = stdscr.getch()
        if player1.is_dead==False:

            if c == ord("d"):
                if player1.x < width-1:
                    player1.set_next_action( player1.move, (player1.x+1,player1.y, maplist,
                                                        gameitems, npcs))

            if c == ord("a"):
                if player1.x > 0:
                    player1.set_next_action( player1.move, (player1.x-1,player1.y, maplist,
                                                        gameitems, npcs))
            if c == ord("w"):
                if player1.y > 0:
                    player1.set_next_action( player1.move, (player1.x,player1.y-1, maplist,
                                                        gameitems, npcs))

            if c == ord("s"):
                if player1.y < height-1:
                    player1.set_next_action( player1.move, (player1.x,player1.y+1, maplist,
                                                        gameitems, npcs))
            #menus
            if c == ord("i") and game_mode==GameMode.game:
                set_active_menu(menus['inventory'])

            if c == ord("l") and game_mode==GameMode.game:
                set_active_menu(menus['log'])
            if c == ord("?") and game_mode==GameMode.game:
                set_active_menu(menus['help'])
            if c == ord("q"):
                close_active_menu()
                set_active_menu(menus['exit'])
                stdscr.clear()
            if active_menu==menus['exit']:
                if c == ord("y"):
                    break
                elif c == ord("n") or c == 27:
                    close_active_menu()
                    stdscr.clear()
            if c == 27: #esc
                if game_mode==GameMode.menu:
                    close_active_menu()
                    stdscr.clear()
            if game_mode == GameMode.game:
                #time to do some action
                if player1.next_action_func != None:
                    player1.do_action()
                    for val in npcs:
                        if val.is_dead == False and val.saw_player and helper.distance(player1, val) < 7:
                            search_way1.wave(val.x, val.y, player1.x, player1.y, npcs, copy.deepcopy(maplist))
                            val.path = search_way1.path
                            val.do_action()
        stdscr.refresh()


curses.wrapper(curses_main)
curses.endwin()
