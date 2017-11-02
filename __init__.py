import curses
import time
import rogmap
import player
import gameitem
import npc
import search_way
import copy
def delay(sleep = 0.1):
    time.sleep(sleep)


"""
Main function

"""
def curses_main(args):




    #setting up curses
    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(True)
    curses.noecho()
    curses.curs_set(0)
    #inits some important values
    rogmap1 = rogmap.rogmap()
    rogmap1.init()
    player1 = player.player(1,1)
    global_msg = "wsad - movement, q - exit"
    search_way1 = search_way.search_way()
    #size of the map
    width = 10
    height = 10

    maplist = rogmap1.getmaplist()

    #add some coins
    gameitems = [gameitem.coin(4, 9), gameitem.coin(6,8)]
    #add some enemies
    npcs = [npc.npc(4,4, "Bob Salem")]
    #all enemies will attack player
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
                    stdscr.addstr(i,j, element)
                j +=1
            i +=1
            j = 0
        #draws items on the map
        for val in gameitems:

            if val.on_the_ground == True:
                stdscr.addstr(val.y,val.x, val.symbol)
        #draws npcs on the map
        for val in npcs:
            if val.is_dead == False:
                stdscr.addstr(val.y, val.x, val.symbol)
        #draws main character
        stdscr.addstr(player1.y,player1.x,"@")
        #adding HUD
        stdscr.addstr(18, 2, "Name: {0} level: {1} HP: {2}/{3} Coins: {4}".format(
        player1.name, player1.level, player1.hp, player1.maxhp, player1.coins))
        stdscr.addstr(20, 2, global_msg)
        #listen to keyinput
        c = stdscr.getch()
        if c == ord('q'):
            break

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
                if val.is_dead == False:
                    search_way1.wave(val.x, val.y, player1.x, player1.y,copy.deepcopy(maplist))
                    val.path = search_way1.path
                    val.do_action()

        stdscr.clear()
        stdscr.refresh()


curses.wrapper(curses_main)
curses.endwin()
