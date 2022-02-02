import unittest

from funcs import guess_number, did_win


class TestFuncs(unittest.TestCase):
    """
    Test class to test funcs module
    """
    
    def test_guess_number(self):
        """
        test guess_number functionality
        """
        # Params
        f_guess = '4'
        f_turns_left = 3
        # Returns
        return_1 = 4
        return_2 = 2
        # Calls
        integer_1, integer_2 = guess_number(f_guess, f_turns_left)
        # Asserts
        self.assertEqual(integer_1, return_1)
        self.assertEqual(integer_2, return_2)

    def test_guess_number_incorrect_integer_range(self):
        """
        test guess_number functionality handles incorrect integer range
        """
        # Params
        f_guess = '-5'
        f_turns_left = 3
        # Returns
        return_1 = '\nRULES: Please enter a number between 1 and 9.'
        return_2 = 2
        # Calls
        string_1, integer_1 = guess_number(f_guess, f_turns_left)
        # Asserts
        self.assertEqual(string_1, return_1)
        self.assertEqual(integer_1, return_2)

    def test_guess_number_non_integer(self):
        """
        test guess_number functionality handles non integer
        """
        # Params
        f_guess = 'k'
        f_turns_left = 3
        # Returns
        return_1 = '\nRULES: Please enter a number between 1 and 9.'
        return_2 = 2
        # Calls
        string_1, integer_1 = guess_number(f_guess, f_turns_left)
        # Asserts
        self.assertEqual(string_1, return_1)
        self.assertEqual(integer_1, return_2)

    def test_did_win(self):
        """
        test did_win functionality
        """
        # Params
        f_guess = 5
        f_correct_answer = 5
        # Returns
        return_1 = 'You won!'
        # Calls
        string_1 = did_win(f_guess, f_correct_answer)
        # Asserts
        self.assertEqual(string_1, return_1)

    def test_did_win_guessed_lower(self):
        """
        test did_win functionality handles guessed lower
        """
        # Params
        f_guess = 4
        f_correct_answer = 5
        # Returns
        return_1 = 'HINT: Higher Than 4'
        # Calls
        string_1 = did_win(f_guess, f_correct_answer)
        # Asserts
        self.assertEqual(string_1, return_1)

    def test_did_win_guessed_higher(self):
        """
        test did_win functionality handles guessed higher
        """
        # Params
        f_guess = 6
        f_correct_answer = 5
        # Returns
        return_1 = 'HINT: Lower Than 6'
        # Calls
        string_1 = did_win(f_guess, f_correct_answer)
        # Asserts
        self.assertEqual(string_1, return_1)

    def test_did_win_non_integer(self):
        """
        test did_win functionality handles non integer
        """
        # Params
        f_guess = 'k'
        f_correct_answer = 5
        # Returns
        return_1 = '\nRULES: Please enter a number between 1 and 9.'
        # Calls
        string_1 = did_win(f_guess, f_correct_answer)
        # Asserts
        self.assertEqual(string_1, return_1)


if __name__ == '__main__':
    unittest.main()
