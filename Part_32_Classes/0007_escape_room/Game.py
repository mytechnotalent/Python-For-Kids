from random import randint, choice


class Game:
    """
    Class to handle game integration
    """

    @staticmethod
    def generate_random_number(grid):
        """
        Method to handle obtaining random number to seed
        the Red Key placement

        Params:
            grid: object

        Returns:
            int, int
        """
        x = randint(1, grid.available_width)
        return x

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
            x = randint(1, grid.available_width)
            y = randint(1, grid.available_width)
        return x, y

    @staticmethod
    def ask_random_question(d_questions):
        """Method to ask a random question from the database

        Params:
            d_questions: dict

        Returns:
            str, str, str, str, int, str
        """
        random_question = choice(list(d_questions))
        answer_1 = d_questions[random_question][0]
        answer_2 = d_questions[random_question][1]
        answer_3 = d_questions[random_question][2]
        correct_answer_index = d_questions[random_question][3]
        correct_answer = d_questions[random_question][correct_answer_index]
        return random_question, answer_1, answer_2, answer_3, correct_answer_index, correct_answer

    @staticmethod
    def correct_answer_response():
        """
        Method to handle correct answer response
        """
        return '\nCorrect!'

    @staticmethod
    def incorrect_answer_response(correct_answer):
        """
        Method to handle incorrect answer logic

        Params:
            correct_answer: str

        Returns:
            str
        """
        return '\nThe correct answer is {0}.'.format(correct_answer)

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
        return '\nYou Escaped!'
