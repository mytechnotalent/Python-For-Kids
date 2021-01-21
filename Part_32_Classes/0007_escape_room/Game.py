from random import randint, choice
from data import questions


class Game:
    """
    Class to handle game integration
    """

    @staticmethod
    def generate_random_numbers(grid):
        """
        Method to handle obtaining random number to place question

        Params:
            grid: object

        Returns:
            int, int
        """
        x = randint(1, grid.available_width)
        y = randint(1, grid.available_height)
        while x == 1 and y == 1:
            x = randint(1, 3)
            y = randint(1, 3)
        return x, y

    @staticmethod
    def __get_random_question():
        """Method to get a random question from the database

        Returns:
            str, str, str, str, str, str
        """
        random_question = choice(list(questions))
        answer_1 = questions[random_question][0]
        answer_2 = questions[random_question][1]
        answer_3 = questions[random_question][2]
        correct_answer_index = questions[random_question][3]
        correct_answer = questions[random_question][correct_answer_index]
        return random_question, answer_1, answer_2, answer_3, correct_answer_index, correct_answer

    def ask_question(self):
        """
        Method to handle ask question logic

        Returns:
             int, int, str
        """
        random_question, answer_1, answer_2, answer_3, correct_answer_index, correct_answer \
            = self.__get_random_question()
        print(random_question)
        print('Press 1 for {0}.'.format(answer_1))
        print('Press 2 for {0}.'.format(answer_2))
        print('Press 3 for {0}.'.format(answer_3))
        while True:
            key = input('Enter 1, 2, 3: ')
            if key == '1':
                response = 0
                break
            elif key == '2':
                response = 1
                break
            elif key == '3':
                response = 2
                break
            else:
                pass
        return response, correct_answer_index, correct_answer

    @staticmethod
    def correct_answer_response():
        """
        Method to handle correct answer response
        """
        return 'Correct!'

    @staticmethod
    def incorrect_answer_response(correct_answer):
        """
        Method to handle correct answer logic

        Params:
            correct_answer: str

        Returns:
            str
        """
        return 'The correct answer is {0}.'.format(correct_answer)

    @staticmethod
    def win(file_manager):
        """
        Method to handle win game logic

        Params:
            file_manager: object

        Returns:
            str
        """
        file_manager.clear_inventory_file()
        return 'You Won!\nYou Escaped!'

    @staticmethod
    def update_ui(grid, player):
        """
        Method to update ui

        Params:
            grid: object
            player: object
        """
        clear_screen = grid.clear_screen()
        print(clear_screen)
        display_grid = grid.update_display(player)
        print(display_grid)
