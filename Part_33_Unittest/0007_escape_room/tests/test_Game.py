import unittest
import mock

from Game import Game
from Grid import Grid
from FileManager import FileManager


class TestGame(unittest.TestCase):
    def setUp(self):
        """
        setUp class
        """
        # Instantiate
        self.game = Game()
        self.grid = Grid()
        self.file_manager = FileManager()

    @mock.patch('Game.randint', return_value=2)
    def test_generate_random_number(self, _):
        """
        test generate_random_number functionality
        """
        # Params
        grid = self.grid

        # Returns
        return_1 = 2

        # Calls
        integer_1 = self.game.generate_random_number(grid)

        # Asserts
        self.assertEqual(integer_1, return_1)

    @mock.patch('Game.randint', return_value=2)
    def test_generate_random_numbers(self, _):
        """
        test generate_random_numbers functionality
        """
        # Params
        grid = self.grid

        # Returns
        return_1 = 2
        return_2 = 2

        # Calls
        integer_1, integer_2 = self.game.generate_random_numbers(grid)

        # Asserts
        self.assertEqual(integer_1, return_1)
        self.assertEqual(integer_2, return_2)

    @mock.patch('Game.choice', return_value='What year did Damien George create MicroPython?')
    def test_ask_random_question(self, _):
        """
        test ask_random_question functionality
        """
        # Params
        d_questions = {
            'What year was the MicroBit educational foundation created?':
                [
                    '2016',
                    '2014',
                    '2017',
                    0
                ],
            'What year was the first computer invented?':
                [
                    '1954',
                    '1943',
                    '1961',
                    1
                ],
            'What year did Damien George create MicroPython?':
                [
                    '2015',
                    '2012',
                    '2014',
                    2
                ],
            'What year did the Commodore 64 get released?':
                [
                    '1983',
                    '1984',
                    '1982',
                    2
                ],
        }

        # Returns
        return_1 = 'What year did Damien George create MicroPython?'
        return_2 = '2015'
        return_3 = '2012'
        return_4 = '2014'
        return_5 = 2
        return_6 = '2014'

        # Calls
        string_1, string_2, string_3, string_4, integer_1, string_5 = self.game.ask_random_question(d_questions)

        # Asserts
        self.assertEqual(string_1, return_1)
        self.assertEqual(string_2, return_2)
        self.assertEqual(string_3, return_3)
        self.assertEqual(string_4, return_4)
        self.assertEqual(integer_1, return_5)
        self.assertEqual(string_5, return_6)

    def test_correct_answer_response(self):
        """
        test correct_answer_response functionality
        """
        # Returns
        return_1 = '\nCorrect!'

        # Calls
        string_1 = self.game.correct_answer_response()

        # Asserts
        self.assertEqual(string_1, return_1)

    def test_incorrect_answer_response(self):
        """
        test incorrect_answer_response functionality
        """
        # Params
        correct_answer = '2014'

        # Returns
        return_1 = '\nThe correct answer is 2014.'

        # Calls
        string_1 = self.game.incorrect_answer_response(correct_answer)

        # Asserts
        self.assertEqual(string_1, return_1)

    def test_win(self):
        """
        test win functionality
        """
        # Params
        file_manager = self.file_manager

        # Returns
        return_1 = '\nYou Escaped!'

        # Calls
        string_1 = self.game.win(file_manager)

        # Asserts
        self.assertEqual(string_1, return_1)


if __name__ == '__main__':
    unittest.main()
