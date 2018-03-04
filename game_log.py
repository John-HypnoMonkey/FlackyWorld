import unittest


class TestGameLog(unittest.TestCase):

    def testAddMessage(self):
        self.assertIsNone(GameLog.addMessage("test"))


class GameLog():
    __history = []
    y = 35
    x = 2
    emptyline = 50 * " "
    num_of_lines = 6

    @classmethod
    def addMessage(cls, message):
        GameLog.__history.append(message)

    @classmethod
    def showLog(cls, stdscr):
        i = 0

        for line in GameLog.__history[::-1]:
            stdscr.addstr(GameLog.y+i, GameLog.x, GameLog.emptyline)
            stdscr.addstr(GameLog.y+i, GameLog.x, line)
            i = i + 1
            if i > GameLog.num_of_lines:
                break

    @classmethod
    def getLog(cls):
        return GameLog.__history


if __name__ == "__main__":
    unittest.main()
