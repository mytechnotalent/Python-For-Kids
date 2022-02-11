from random import randint, choice
from microbit import display, Image
from speech import say
import music

from data import questions
from file_manager import FileManager


class Game:
    """
    Class to handle game integration
    """

    def __init__(self):
        self.SAY_SPEED = 95
        self.final_question = False
        self.random_question = None
        self.answer_1 = None
        self.answer_2 = None
        self.answer_3 = None
        self.correct_answer_index = None
        self.correct_answer = None
        self.file_manager = FileManager()
        self.__instructions()

    @staticmethod
    def __generate_random_number(grid):
        """
        Private static method to handle obtaining random number

        Params:
            grid: object

        Returns:
            int
        """
        x = randint(1, grid.available_width)
        return x

    @staticmethod
    def __generate_random_numbers(grid):
        """
        Private static method to handle obtaining random numbers

        Params:
            grid: object

        Returns:
            int, int
        """
        x = randint(1, grid.available_width)
        y = randint(1, grid.available_height)
        while x == 1 and y == 1:
            x = randint(1, grid.available_width)
            y = randint(1, grid.available_width)
        return x, y

    @staticmethod
    def __correct_answer_response():
        """
        Private static method to handle correct answer response

        Returns:
            str
        """
        return '\nCorrect!'
    
    def __instructions(self):
        """
        Private method to give instructions to the player
        """
        display.show(Image.SURPRISED)
        say('Welcome to the Escape Room!', speed=self.SAY_SPEED)
        say('Press the aay button to move west.', speed=self.SAY_SPEED)
        say('Press the lowgo to move north.', speed=self.SAY_SPEED)
        say('Press the bee button to move east.', speed=self.SAY_SPEED)
        say('Press pin two to move south.', speed=self.SAY_SPEED)
        say('Good luck!', speed=self.SAY_SPEED)
        say('Let the games begin!', speed=self.SAY_SPEED)
    
    def __ask_random_question(self, d_questions):
        """
        Private method to ask a random question from the database

        Params:
            d_questions: dict
        """
        self.random_question = choice(list(d_questions))
        self.answer_1 = d_questions[self.random_question][0]
        self.answer_2 = d_questions[self.random_question][1]
        self.answer_3 = d_questions[self.random_question][2]
        self.correct_answer_index = d_questions[self.random_question][3]
        self.correct_answer = d_questions[self.random_question][self.correct_answer_index]

    def __incorrect_answer_response(self):
        """
        Private method to handle incorrect answer logic

        Params:
            correct_answer: str

        Returns:
            str
        """
        return '\nIncorret.  The correct answer is {0}.'.format(self.correct_answer)

    def __win(self):
        """
        Private method to handle win game logic

        Returns:
            str
        """
        self.file_manager.clear_inventory_file()
        return '\nYou Escaped!'

    def generate_question(self, grid, player):
        """
        Method to generate a question

        Params:
            grid: object
            player: object

        Returns:
            bool
        """
        self.__ask_random_question(questions)
        random_location = (x, y) = self.__generate_random_numbers(grid)
        if self.random_question and random_location == player.location:
            display.show(Image.SURPRISED)
            say('You found gold!', speed=self.SAY_SPEED)
            say('Answer the question correctly.', speed=self.SAY_SPEED)
            say(self.random_question, speed=self.SAY_SPEED)
            say('Press the aay button for {0}.'.format(self.answer_1), speed=self.SAY_SPEED)
            say('Press the lowgo for {0}.'.format(self.answer_2), speed=self.SAY_SPEED)
            say('Press the bee button for {0}.'.format(self.answer_3), speed=self.SAY_SPEED)
            display.show(Image.HAPPY)
            return True
        else:
            return False
                    
    def did_player_win(self, grid, player, player_response):
        """
        Method to handle the check if player won

        Params:
            grid: object
            player: object
            player_response: int

        Returns:
            bool
        """
        if isinstance(self.correct_answer_index, int):
            if player_response == self.correct_answer_index + 1:
                display.show(Image.SURPRISED)
                say(self.__correct_answer_response(), speed=self.SAY_SPEED)
                inventory = player.get_inventory(self.file_manager)
                player.inventory.append(inventory)
                if 'Red Key' in player.inventory:
                    display.show(Image.SURPRISED)
                    say(self.__win(), speed=self.SAY_SPEED)
                    music.play(music.POWER_UP)
                    display.show(Image.ALL_CLOCKS, loop=False, delay=100)
                    return True
                elif 'Red Key' not in player.inventory and not self.final_question:
                    receive_red_key = self.__generate_random_number(grid)
                    if receive_red_key == 2:
                        display.show(Image.SURPRISED)
                        say(player.pick_up_red_key(self.file_manager), speed=self.SAY_SPEED)
                        self.final_question = True
                        return False
                    else:
                        display.show(Image.SURPRISED)
                        say(player.without_red_key(), speed=self.SAY_SPEED)
                        return False
            else:
                display.show(Image.SURPRISED)
                say(self.__incorrect_answer_response(), speed=self.SAY_SPEED)
                return False
    
