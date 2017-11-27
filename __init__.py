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
def curses_main(args):
    #setting up curses
    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(True)
    curses.noecho()
    curses.start_color()
    curses.use_default_colors()
    for i in range(0,curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    curses.curs_set(0)
    #inits some important values
    rogmap1 = rogmap.rogmap()
    rogmap1.init()
    game_objects = []
    player1 = player.player(1,1)
    game_objects.append(player1)
    npcs = []
    gameitems = []
    global_msg = "wsad - movement, q - exit"
    search_way1 = search_way.search_way()
    #size of the map
    width = 63
    height = 31

    maplist = rogmap1.getmaplist()
    #find some place for our hero
    player1.x, player1.y = set_random_position(maplist, game_objects)
    #add some coins
    random_count = random.randint(10,20)
    for i in range(0, random_count):
        x,y = set_random_position(maplist, game_objects)
        gameitems.append(gameitem.coin(x,y))
        game_objects.append(gameitems[-1])
    #add heal potions
    random_count = random.randint(3,5)
    for i in range(0, random_count):
        x,y = set_random_position(maplist, game_objects)
        gameitems.append(gameitem.heal_potion(x,y))
        game_objects.append(gameitems[-1])
    #add some enemies
    random_count = random.randint(3,5)
    for i in range(0,random_count):
        x,y = set_random_position(maplist, game_objects)
        npcs.append(npc.npc(x,y,"Soldier"))
        game_objects.append(npcs[-1])
    #all enemies will player
    for val in npcs:
        val.set_enemy(player1)
    #main loop
    while True:
        #drawing a map
        i = 0
        j = 0
        for row in maplist:
            for element in row:
                if element != '-':
                    if  distance2(player1, j, i) < 7:
                        element_color = 8
                    else:
                        element_color = 7
                    stdscr.addstr(i,j, element, curses.color_pair(element_color))
                else:
                    stdscr.addstr(i,j, ' ')
                j +=1
            i +=1
            j = 0
        #draws items on the map
        for val in gameitems:

            if (distance(player1, val)) < 7 and val.on_the_ground == True:
                stdscr.addstr(val.y,val.x, val.symbol, curses.color_pair(3))
       #draws npcs on the map
        for val in npcs:
            if  (distance(player1, val)) < 7 and val.is_dead == False:
                stdscr.addstr(val.y, val.x, val.symbol, curses.color_pair(2))

        if player1.is_dead == True:
            global_msg="You are dead. Press 'q' to exit"
        else:
            #draws main character
            stdscr.addstr(player1.y,player1.x,"@", curses.color_pair(4))
        #adding HUD
        stdscr.addstr(36, 2, "Name: {0} level: {1} HP: {2}/{3} Coins: {4}".format(
        player1.name, player1.level, player1.hp, player1.maxhp, player1.coins))
        stdscr.addstr(38, 2, global_msg)

        #listen to keyinput
        c = stdscr.getch()
        if player1.is_dead==False:

            if c == ord("d"):
                if player1.x < width-1:
                    player1.set_next_action( player1.move, (player1.x+1,player1.y, maplist,
                                                        gameitems, npcs))

            if c ==ord("a"):
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

            #time to do some action
            if player1.next_action_func != None:
                player1.do_action()
                for val in npcs:
                    if val.is_dead == False and val.saw_player and distance(player1, val) < 7:
                        search_way1.wave(val.x, val.y, player1.x, player1.y,copy.deepcopy(maplist))
                        val.path = search_way1.path
                        val.do_action()
        if c == ord('q'):
            break
      #  stdscr.clear()
        stdscr.refresh()


curses.wrapper(curses_main)
curses.endwin()
