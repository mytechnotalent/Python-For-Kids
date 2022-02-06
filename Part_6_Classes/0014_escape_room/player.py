from time import sleep


class Player:
    """
    Base class to represent a generic player
    """

    def __init__(self, name, dx, dy, location=None, armour=None, inventory=None):
        """
        Params:
            name: str
            dx: int
            dy: int
            location: tuple, optional
            armour = list, optional
            inventory: list, optional 
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
        self.location = location

    def __move(self, dx, dy):
        """
        Private method to move a generic player based on their current x and y location

        Params:
            dx: int
            dy: int
        """
        self.dx += dx
        self.dy += dy
    
    @staticmethod
    def get_inventory(file_manager):
        """
        Static method to get the player inventory from disk

        Params:
            file_manager: object

        Returns:
            str
        """
        inventory = file_manager.read_inventory_file()
        return inventory
    
    def move_east(self, grid):
        """
        Method to move the player east one position

        Params:
            grid: object
        """
        if self.dx < grid.available_width:
            self.__move(dx=1, dy=0)
        sleep(0.25)
        self.location = self.dx, self.dy
        grid.update(self)

    def move_west(self, grid):
        """
        Method to move the player east one position

        Params:
            grid: object
        """
        # If the  player is against the left wall do NOT allow them to go through it
        if self.dx != 1 and self.dx <= grid.available_width:
            self.__move(dx=-1, dy=0)
        sleep(0.25)
        self.location = self.dx, self.dy
        grid.update(self)

    def move_north(self, grid):
        """
        Method to move the player north one position

        Params:
            grid: object
        """
        # If the player is against the top wall do NOT allow them to go through it
        if self.dy != 1 and self.dy <= grid.available_height:
            self.__move(dx=0, dy=-1)
        sleep(0.25)
        self.location = self.dx, self.dy
        grid.update(self)

    def move_south(self, grid):
        """
        Method to move the player south one position

        Params:
            grid: object
        """
        if self.dy < grid.available_height:
            self.__move(dx=0, dy=1)
        sleep(0.25)
        self.location = self.dx, self.dy
        grid.update(self)
