import curses
import rogmap
import player
import gameitem
import npc
import search_way
import copy
import random
import raycast
import helper
import game_log
import menu
import inventory


def drawMultiLineText(stdscr, text, x, y):
    i = 0
    for item in text.split('\n'):
        stdscr.addstr(y+i, x, item)
        i += 1


def drawLogo(stdscr, y=15, x=20):
    logo = (
            "███████╗██╗      █████╗  ██████╗██╗  ██╗██╗   ██╗    ██╗    ██╗ ██████╗ ██████╗ ██╗     ██████╗ \n"
            "██╔════╝██║     ██╔══██╗██╔════╝██║ ██╔╝╚██╗ ██╔╝    ██║    ██║██╔═══██╗██╔══██╗██║     ██╔══██╗\n"
            "█████╗  ██║     ███████║██║     █████╔╝  ╚████╔╝     ██║ █╗ ██║██║   ██║██████╔╝██║     ██║  ██║\n"
            "██╔══╝  ██║     ██╔══██║██║     ██╔═██╗   ╚██╔╝      ██║███╗██║██║   ██║██╔══██╗██║     ██║  ██║\n"
            "██║     ███████╗██║  ██║╚██████╗██║  ██╗   ██║       ╚███╔███╔╝╚██████╔╝██║  ██║███████╗██████╔╝\n"
            "╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝        ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ \n"
            "\n"
            "                                      [a] Start new game\n"
            "                                      [q] Exit\n"
           )
    drawMultiLineText(stdscr, logo, x, y)


class GameMode:
    game, menu, start_screen = range(3)


def drawInventory(stdscr, x, y):
    x2 = x + 5
    y2 = y + 3
    i = 0
    for item in inventory.Inventory.items:
        result = "{0}) {1}".format(helper.ALPHABET[i], item.name)
        if item.count > 1:
            result = "{0} ({1})".format(result, item.count)
        stdscr.addstr(y2+i, x2, result)
        i += 1


def drawWield(stdscr, x, y):
    x2 = x + 5
    y2 = y + 3
    i = 0
    for item in inventory.Inventory.items:
        if isinstance(item, gameitem.Weapon):
            result = "{0}) {1}".format(helper.ALPHABET[i], item.name)
            if item.count > 1:
                result = "{0} ({1})".format(result, item.count)
            stdscr.addstr(y2+i, x2, result)
            i += 1


def drawLog(stdscr, x, y):
    x2 = x + 5
    y2 = y + 3
    log = game_log.GameLog.getLog()
    i = 0
    for item in log[::-1]:
        stdscr.addstr(y2+i, x2, item)
        i += 1
        if i > 25:
            break


def drawHelp(stdscr, x, y):
    x2 = x+5
    y2 = y+3
    helpinfo = ("Welcome to my roguelike.\n"
                "Use num4, num8, num6 and num2 to move.\n"
                "'@' is your character\n"
                "'g' are your enemies\n"
                "',', '$' are items what you can pickup\n"
                "Press 'i' to open inventory, and 'l' to open log\n"
                "Press 'q' to exit the game\n"
                )
    drawMultiLineText(stdscr, helpinfo, x2, y2)



def drawExitMessage(stdscr, x, y):
    x2 = x + 5
    y2 = y + 2
    message = "Do you realy want to exit? y/n"
    stdscr.addstr(y2, x2, message)


def cursesMain(args):

    def closeActiveMenu():
        nonlocal active_menu, game_mode
        if active_menu is not None:
            active_menu.is_visible = False
            active_menu = None
        game_mode = GameMode.game

    def setActiveMenu(item_menu):
        nonlocal active_menu, game_mode
        item_menu.is_visible = True
        active_menu = item_menu
        game_mode = GameMode.menu

    def wieldUpdate():
        pass

    def drawEquipment(stdscr, x, y):
        nonlocal player1
        x2 = x + 5
        y2 = y + 5
        message = ("HEAD    {0}\n"
                   "NECK    {1}\n"
                   "L.ARM   {2}\n"
                   "R.ARM   {3}\n"
                   "TORSO   {4}\n"
                   "LEGS    {5}\n"

                   ).format(player1.equipment['HEAD'],
                            player1.equipment['NECK'],
                            player1.equipment['L.ARM'],
                            player1.equipment['R.ARM'],
                            player1.equipment['TORSO'],
                            player1.equipment['LEGS'])

        i = 0
        for item in message.split('\n'):
            stdscr.addstr(y2 + i, x2, item)
            i += 1

    # setting up curses
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
    curses.curs_set(0)
    # inits some important values

    # inits menu windows
    menus = {}
    menus['log'] = menu.PopUpWindow(stdscr, name="log", draw_func=drawLog)
    menus['inventory'] = menu.PopUpWindow(stdscr, name="inventory", draw_func=drawInventory)
    menus['help'] = menu.PopUpWindow(stdscr, name="help", draw_func=drawHelp)
    menus['wield'] = menu.PopUpWindow(stdscr, name="wield", draw_func=drawWield)
    menus['equipment'] = menu.PopUpWindow(stdscr, name="equipment", draw_func=drawEquipment)
    menus['exit'] = menu.PopUpWindow(stdscr, 25, 15, 40, 4, "exit the game", drawExitMessage)
    active_menu = None
    # set game mode
    game_mode = GameMode.start_screen
    rogmap1 = rogmap.Rogmap()
    rogmap1.init()
    game_objects = []
    player1 = player.Player(1, 1)
    game_objects.append(player1)
    npcs = []
    gameitems = []
    game_log.GameLog.addMessage("Press '?' for help")
    search_way1 = search_way.SearchWay()
    # size of the map
    width = 63
    height = 31

    maplist = rogmap1.getMapList()
    # find some place for our hero
    player1.x, player1.y = helper.setRandomPosition(maplist, game_objects)

    def addItemsToMap(item_class, min_count, max_count, room=None):
        nonlocal maplist, game_objects, gameitems
        random_count = random.randint(min_count, max_count)
        for i in range(0, random_count):
            x, y = helper.setRandomPosition(maplist, game_objects)
            gameitems.append(item_class(x, y))
            game_objects.append(gameitems[-1])

    def addNpcsToMap(npc_class, min_count, max_count, room=None):
        nonlocal maplist, game_objects, npcs
        random_count = random.randint(min_count, max_count)
        for i in range(0, random_count):
            x, y = helper.setRandomPosition(maplist, game_objects)
            npcs.append(npc_class(x, y, helper.getRandomName()))
            game_objects.append(npcs[-1])

    addItemsToMap(gameitem.Sword, 3, 3)
    addItemsToMap(gameitem.Club, 5, 7)
    # add some coins
    addItemsToMap(gameitem.Coin, 10, 20)
    # add heal potions
    addItemsToMap(gameitem.HealPotion, 5, 10)
    # add some enemies
    addNpcsToMap(npc.Goblin, 5, 7)
    addNpcsToMap(npc.GoblinCapitan, 1, 3)
    # all enemies will chase player
    for val in npcs:
        val.setEnemy(player1)
    # main loop
    while True:
        if game_mode == GameMode.start_screen:
            drawLogo(stdscr)
        else:
            # drawing a map
            raycast.raycast(stdscr, maplist, game_objects, player1.x, player1.y)

            if player1.is_dead is True:
                game_log.GameLog.addMessage("You are dead. Press 'q' to exit")
            else:
                # draws main character
                stdscr.addstr(player1.y, player1.x, "@",
                              curses.color_pair(helper.COLOR_YELLOW))
            # adding HUD
            stdscr.addstr(32, 2, "Name: {0} level: {1} HP: {2}/{3} Coins: {4}".
                          format(player1.name, player1.level, player1.hp,
                                 player1.maxhp, player1.coins))
            # stdscr.addstr(38, 2, global_msg)

            # show message log
            game_log.GameLog.showLog(stdscr)

            for key in menus:
                menus[key].draw()
        # listen to keyinput
        c = stdscr.getch()
        if game_mode == GameMode.start_screen:
            # start new game
            if c == ord("a"):
                game_mode = GameMode.game
                stdscr.clear()
            if c == ord("q"):
                # exit the game
                break
        else:
            if player1.is_dead is False:

                if c == ord("6"):
                    if player1.x < width-1:
                        player1.setNextAction(player1.move,
                                              (player1.x+1, player1.y, maplist,
                                               gameitems, npcs))

                if c == ord("4"):
                    if player1.x > 0:
                        player1.setNextAction(player1.move,
                                              (player1.x-1, player1.y, maplist,
                                               gameitems, npcs))
                if c == ord("8"):
                    if player1.y > 0:
                        player1.setNextAction(player1.move,
                                              (player1.x, player1.y-1, maplist,
                                               gameitems, npcs))

                if c == ord("2"):
                    if player1.y < height-1:
                        player1.setNextAction(player1.move,
                                              (player1.x, player1.y+1, maplist,
                                               gameitems, npcs))
                # menus
                if c == ord("i") and game_mode == GameMode.game:
                    setActiveMenu(menus['inventory'])

                if c == ord("l") and game_mode == GameMode.game:
                    setActiveMenu(menus['log'])
                if c == ord("?") and game_mode == GameMode.game:
                    setActiveMenu(menus['help'])
                if c == ord("w") and game_mode == GameMode.game:
                    setActiveMenu(menus['wield'])
                    continue
                if c == ord("e") and game_mode == GameMode.game:
                    setActiveMenu(menus['equipment'])
                if c == ord("q"):
                    closeActiveMenu()
                    setActiveMenu(menus['exit'])
                    stdscr.clear()
                if active_menu == menus['wield']:
                    char = chr(c)
                    game_log.GameLog.addMessage(char)
                if active_menu == menus['exit']:
                    if c == ord("y"):
                        break
                    elif c == ord("n") or c == 27:
                        closeActiveMenu()
                        stdscr.clear()
                # esc
                if c == 27:
                    if game_mode == GameMode.menu:
                        closeActiveMenu()
                        stdscr.clear()
                if game_mode == GameMode.game:
                    # time to do some action
                    if player1.next_action_func is not None:
                        player1.doAction()
                        for val in npcs:
                            if val.is_dead is False and val.saw_player \
                               and helper.distance(player1, val) < 7:
                                search_way1.wave(val.x, val.y, player1.x,
                                                 player1.y, npcs, copy.deepcopy(maplist))
                                val.path = search_way1.path
                                val.doAction()
        stdscr.refresh()


curses.wrapper(cursesMain)
curses.endwin()
