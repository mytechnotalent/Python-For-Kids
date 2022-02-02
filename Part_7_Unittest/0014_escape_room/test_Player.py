import unittest

from player import Player
from grid import Grid
from file_manager import FileManager


class TestPlayer(unittest.TestCase):
    """
    Test class to test player module
    """
    
    def setUp(self):
        """
        setUp class
        """
        # Instantiate
        self.player = Player()
        self.grid = Grid()
        self.file_manager = FileManager()

    def test_move_east(self):
        """
        test move_east functionality
        """
        # Params
        grid = self.grid
        # Returns
        return_1 = self.player.dx
        return_2 = self.player.dy
        # Calls
        integer_1, integer_2 = self.player.move_east(grid)
        # Asserts
        self.assertEqual(integer_1, return_1)
        self.assertEqual(integer_2, return_2)

    def test_move_west(self):
        """
        test move_west functionality
        """
        # Returns
        return_1 = self.player.dx
        return_2 = self.player.dy
        # Calls
        integer_1, integer_2 = self.player.move_west(self.grid)
        # Asserts
        self.assertEqual(integer_1, return_1)
        self.assertEqual(integer_2, return_2)

    def test_move_north(self):
        """
        test move_north functionality
        """
        # Params
        grid = self.grid
        # Returns
        return_1 = self.player.dx
        return_2 = self.player.dy
        # Calls
        integer_1, integer_2 = self.player.move_north(grid)
        # Asserts
        self.assertEqual(integer_1, return_1)
        self.assertEqual(integer_2, return_2)

    def test_move_south(self):
        """
        test move_south functionality
        """
        # Params
        grid = self.grid
        # Returns
        return_1 = self.player.dx
        return_2 = self.player.dy
        # Calls
        integer_1, integer_2 = self.player.move_south(grid)
        # Asserts
        self.assertEqual(integer_1, return_1)
        self.assertEqual(integer_2, return_2)

    def test_get_inventory(self):
        """
        test get_inventory functionality
        """
        # Params
        file_manager = self.file_manager
        # Returns
        return_1 = ''
        # Calls
        string_1 = self.player.get_inventory(file_manager)
        # Asserts
        self.assertEqual(string_1, return_1)


if __name__ == '__main__':
    unittest.main()
