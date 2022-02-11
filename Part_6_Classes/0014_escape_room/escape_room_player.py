from player import Player


class EscapeRoomPlayer(Player):
    """
    Child class to represent an escape room player
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

    @staticmethod
    def pick_up_red_key(game):
        """
        Static method to handle picking up red key

        Params:
            game: object

        Returns:
            str
        """
        game.write_inventory_file('Red Key')
        return 'You picked up the red key!'

    @staticmethod
    def without_red_key():
        """
        Static method to handle not having the red key

        Returns:
            str
        """
        return 'You do not have the red key to escape.'
