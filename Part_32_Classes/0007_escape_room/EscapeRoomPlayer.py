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

    @staticmethod
    def pick_up_red_key(file_manager):
        """
        Method to handle picking up red key

        Params:
            file_manager: object

        Returns:
            str
        """
        file_manager.write_inventory_file('Red Key')
        return 'You picked up the red key!'

    @staticmethod
    def without_red_key():
        """
        Method to handle not having the red key

        Returns:
            str
        """
        return 'You do not have the red key to escape.'
