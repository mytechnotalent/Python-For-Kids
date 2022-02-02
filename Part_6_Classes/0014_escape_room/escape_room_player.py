from player import Player


class EscapeRoomPlayer(Player):
    """
    Child class to represent an escape room player inheriting from the Player base class
    """

    def __init__(self, name, dx=1, dy=1, location=None):
        """
        Parms:
            name: str
            dx: int, optional
            dy: int, optional
            location: tuple, optional
        """
        super().__init__(name, dx, dy, location)

    def pick_up_red_key(self, file_manager):
        """
        Method to handle picking up red key

        Params:
            file_manager: object

        Returns:
            str
        """
        file_manager.write_inventory_file('Red Key')
        return 'You picked up the red key!'

    def without_red_key(self):
        """
        Method to handle not having the red key

        Returns:
            str
        """
        return 'You do not have the red key to escape.'
