import unittest

from grid import Grid
from escape_room_player import EscapeRoomPlayer


class TestGrid(unittest.TestCase):
    """
    Test class to test grid module
    """
    
    def setUp(self):
        """
        setUp class
        """
        # Instantiate
        self.grid = Grid()
        self.player = EscapeRoomPlayer()

    def test_update(self):
        """
        test update functionality
        """
        # Params
        self.player.dx = 0
        self.player.dy = 0
        player = self.player
        # Returns
        return_1 = '9\n'
        # Calls
        string_1 = self.grid.update(player)
        # Asserts
        self.assertEqual(string_1, return_1)


if __name__ == '__main__':
    unittest.main()
