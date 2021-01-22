from Player import Player


class EscapeRoomPlayer(Player):
    """
    Child class to represent an escape room player inheriting from the Player base class
    """

    def __init__(self, name=None, dx=1, dy=1, armour=None, inventory=None):
        """
        Attrs:
            name: str
            dx: int
            dy: int
            armour = list
            inventory: list
        """
        super().__init__(name, dx, dy, armour, inventory)

    def keyboard_a_press(self, grid):
        """
        Method to handle a keyboard a press

        Params:
            grid: object

        Returns:
            int, int
        """
        # If player is against the left wall do NOT allow them to go through it
        if self.dx != 1 and self.dx <= grid.available_width:
            self.move_west()
        return self.dx, self.dy

    def keyboard_d_press(self, grid):
        """
        Method to handle a keyboard d press

        Params:
            grid: object

        Returns:
            int, int
        """
        if self.dx < grid.available_width:
            self.move_east()
        return self.dx, self.dy

    def keyboard_w_press(self, grid):
        """
        Method to handle a keyboard w press

        Params:
            grid: object

        Returns:
            int, int
        """
        # If badge player is against the top wall do NOT allow them to go through it
        if self.dy != 1 and self.dy <= grid.available_width:
            self.move_north()
        return self.dx, self.dy

    def keyboard_s_press(self, grid):
        """
        Method to handle a keyboard s press

        Params:
            grid: object

        Returns:
            int, int
        """
        if self.dy < grid.available_height:
            self.move_south()
        return self.dx, self.dy

    @staticmethod
    def get_inventory(self, file_manager):
        """
        Method to get the inventory from disk

        Params:
            file_manager: object

        Returns:
            str
        """
        inventory = file_manager.read_inventory_file()
        return inventory

    @staticmethod
    def pick_up_red_key(file_manager):
        """
        Method to handle picking up red key

        Params:
            file_manager: object
        """
        file_manager.write_inventory_file('Red Key')
        return 'You picked up the red key!'

    @staticmethod
    def without_red_key():
        """
        Method to handle not having the red key
        """
        return 'You do not have the red key to escape.'
