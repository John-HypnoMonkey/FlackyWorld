import curses
import unittest

class TestGameLog(unittest.TestCase):
    def test_add_message(self):
        self.assertIsNone(game_log.add_message("test"))
class game_log():
    __history = []
    y = 35
    x = 2
    emptyline =50*" "
    @classmethod
    def add_message(cls, message):
        game_log.__history.append(message)
    @classmethod
    def show_log(cls, stdscr):
        i=0

        for line in game_log.__history[::-1]:
            stdscr.addstr(game_log.y+i, game_log.x, game_log.emptyline)
            stdscr.addstr(game_log.y+i, game_log.x, line)
            i = i +1
            if i >10:
                break

if __name__ == "__main__":
    unittest.main()
