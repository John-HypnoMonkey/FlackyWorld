import curses


class pop_up_window():
    # all draw_func must have (stdscr, x, y) signature
    def __init__(self, stdscr, x=10, y=10, width=100, height=30,
                 name="pop-up window", draw_func=None, update_func=None):
        self.stdscr = stdscr
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name
        self.draw_func = draw_func
        self.update_func = update_func
        self.is_visible = False
        # horizontal line
        self.top_h_line = u'\u250c{0}\u2510'.format((self.width-2)*u'\u2500')
        self.bottom_h_line = u'\u2514{0}\u2518'.format((self.width-2)*u'\u2500')
        self.blank_space = (self.width-4)*' '
        self.content_line = u'\u2502 {0} \u2502'.format(self.blank_space)

    def draw(self):
        if self.is_visible is True:
            self.stdscr.addstr(self.y, self.x, self.top_h_line)
            self.stdscr.addstr(self.y, self.x + 5, self.name)
            for i in range(1, self.height):
                self.stdscr.addstr(self.y + i, self.x, self.content_line)
            self.stdscr.addstr(self.y + self.height, self.x, self.bottom_h_line)
            self.draw_func(self.stdscr, self.x, self.y)

    def update(self):
        self.update_func()


if __name__ == '__main__':
    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(True)
    curses.noecho()
    curses.start_color()
    curses.use_default_colors()
    curses.curs_set(0)
    window1 = pop_up_window(stdscr, 10, 10, 100, 30, 'Inventory')
    window1.is_visible = True

    while True:
        window1.draw()
        c = stdscr.getch()
        if c == ord("q"):
            break
