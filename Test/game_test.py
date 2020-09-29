import unittest
from src.Game.Game import Game

class MyTestCase(unittest.TestCase):
    def test_game(self):
        game = Game()
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
