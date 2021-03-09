from time import sleep


class Player:
    """
    Base class to represent a generic player
    """

    def __init__(self, name='Generic', dx=0, dy=0, armour=None, inventory=None):
        """
        Attrs:
            name: str
            dx: int
            dy: int
            armour = list
            inventory: list
        """
        self.name = name
        self.dx = dx
        self.dy = dy
        if armour is None:
            armour = []
        self.armour = armour
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def __move(self, dx, dy):
        """Method to move a generic player based on their current x and y location

        Params:
            dx: int
            dy: int
        """
        self.dx += dx
        self.dy += dy

    def __move_north(self):
        """
        Method to move a generic player from their current position to one position north
        """
        self.__move(dx=0, dy=-1)

    def __move_south(self):
        """
        Method to move a generic player from their current position to one position south
        """
        self.__move(dx=0, dy=1)

    def __move_east(self):
        """
        Method to move a generic player from their current position to one position east
        """
        self.__move(dx=1, dy=0)

    def __move_west(self):
        """
        Method to move a generic player from their current position to one position west
        """
        self.__move(dx=-1, dy=0)

    def move_east(self, grid):
        """
        Method to move the player east one position

        Params:
            grid: object

        Returns:
            int, int
        """
        if self.dx < grid.available_width:
            self.__move_east()
        sleep(0.25)
        return self.dx, self.dy

    def move_west(self, grid):
        """
        Method to move the player east one position

        Params:
            grid: object

        Returns:
            int, int
        """
        # If the  player is against the left wall do NOT allow them to go through it
        if self.dx != 1 and self.dx <= grid.available_width:
            self.__move_west()
        sleep(0.25)
        return self.dx, self.dy

    def move_north(self, grid):
        """
        Method to move the player north one position

        Params:
            grid: object

        Returns:
            int, int
        """
        # If the player is against the top wall do NOT allow them to go through it
        if self.dy != 1 and self.dy <= grid.available_height:
            self.__move_north()
        sleep(0.25)
        return self.dx, self.dy

    def move_south(self, grid):
        """
        Method to move the player south one position

        Params:
            grid: object

        Returns:
            int, int
        """
        if self.dy < grid.available_height:
            self.__move_south()
        sleep(0.25)
        return self.dx, self.dy

    @staticmethod
    def get_inventory(file_manager):
        """
        Method to get the player inventory from disk

        Params:
            file_manager: object

        Returns:
            str
        """
        inventory = file_manager.read_inventory_file()
        return inventory
