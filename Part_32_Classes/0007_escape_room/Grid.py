class Grid:
    """
    Class to represent a generic grid
    """

    def __init__(self, led_height=0, led_width=0, led_on='*', led_off=' '):
        """
        Attrs:
            led_height: int
            led_width: int
            led_on: int
            led_off: int
        """
        self.led_height = led_height
        self.led_width = led_width
        self.led_on = led_on
        self.led_off = led_off
        self.available_height = led_height - 2
        self.available_width = led_width - 2

    @staticmethod
    def clear_screen():
        """
        Method to clear terminal

        Returns:
            str
        """
        return '\n' * 100

    def draw_grid(self):
        """
        Method to draw grid on generic led display

        Returns:
             str, str, str
        """
        top_wall = self.led_on * self.led_width + '\n'
        side_walls = ''
        for _ in range(self.available_height):
            side_walls += self.led_on + self.led_off * self.available_width + self.led_on + '\n'
        bottom_wall = self.led_on * self.led_width
        return top_wall, side_walls, bottom_wall

    def update_display(self, player):
        """
        Update display with each event where we re-draw
        grid with player's current position

        Params:
            player: object

        Returns:
            grid: str
        """
        top_wall, side_walls, bottom_wall = self.draw_grid()
        grid = top_wall + side_walls + bottom_wall + '\n'
        temp_grid = list(grid)
        if player.dx == 1:
            temp_grid[self.led_width + player.dx + player.dy] = '*'
        grid = ''
        grid = grid.join(temp_grid)
        return grid
