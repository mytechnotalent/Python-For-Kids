import unittest

from chocolate_machine import ChocolateMachine
from data import CHOCOLATE_CHOICES


class TestChocolateMachine(unittest.TestCase):
    """
    Test class to test chocolate_machine module
    """
    
    def setUp(self):
        """
        setUp class
        """
        # Instantiate
        CHOICES = ('dark', 'caramel', 'mint', 'surprise', 'stats', 'shutdown')
        choice = 'dark'
        self.chocolate_machine = ChocolateMachine(CHOICES)
        self.selection = CHOCOLATE_CHOICES[choice]

    def test_stats(self):
        """
        test stats functionality
        """
        # Params
        d_raw_materials = {
            'sugar': 2,
            'butter': 2,
            'caramel': 15,
            'dark chocolate': 30,
            'mint chocolate': 30,
            'milk chocolate': 30,
            'light corn syrup': 2,
            'sweetened condensed milk': 2,
            'vanilla extract': 2,
            'Reese\'s Pieces': 15,
        }
        # Returns
        return_1 = 'sugar 2 tablespoons remaining\n' \
            'butter 2 teaspoons remaining\n' \
            'dark chocolate 30 tablespoons remaining\n' \
            'mint chocolate 30 tablespoons remaining\n' \
            'milk chocolate 30 tablespoons remaining\n' \
            'light corn syrup 2 teaspoons remaining\n' \
            'sweetened condensed milk 2 teaspoons remaining\n' \
            'vanilla extract 2 teaspoons remaining\n' \
            'Reese\'s Pieces 15 tablespoons remaining\n' \
            'Total Money Collected: $0.00\n'
        # Calls
        string_1 = self.chocolate_machine.stats(d_raw_materials)
        # Asserts
        self.assertEqual(string_1, return_1)

    def test_has_raw_materials(self):
        """
        test has_raw_materials functionality
        """
        # Params
        m_raw_materials = self.selection['ingredients']
        d_raw_materials = {
            'sugar': 2,
            'butter': 2,
            'caramel': 15,
            'dark chocolate': 30,
            'mint chocolate': 30,
            'milk chocolate': 30,
            'light corn syrup': 2,
            'sweetened condensed milk': 2,
            'vanilla extract': 2,
            'Reese\'s Pieces': 15,
        }
        # Returns
        return_1 = True
        # Calls
        bool_1 = self.chocolate_machine.has_raw_materials(m_raw_materials, d_raw_materials)
        # Asserts
        self.assertEqual(bool_1, return_1)

    def test_has_raw_materials_handles_insufficient_raw_materials(self):
        """
        test has_raw_materials handles insufficient raw materials functionality
        """
        # Params
        m_raw_materials = self.selection['ingredients']
        d_raw_materials = {
            'sugar': 0,
            'butter': 0,
            'caramel': 15,
            'dark chocolate': 0,
            'mint chocolate': 30,
            'milk chocolate': 30,
            'light corn syrup': 0,
            'sweetened condensed milk': 0,
            'vanilla extract': 0,
            'Reese\'s Pieces': 15,
        }
        # Returns
        return_1 = 'Machine Needs Additional: sugar\n' \
                   'Machine Needs Additional: butter\n' \
                   'Machine Needs Additional: dark chocolate\n' \
                   'Machine Needs Additional: light corn syrup\n' \
                   'Machine Needs Additional: sweetened condensed milk\n' \
                   'Machine Needs Additional: vanilla extract\n'
        # Calls
        bool_1 = self.chocolate_machine.has_raw_materials(m_raw_materials, d_raw_materials)
        # Asserts
        self.assertEqual(bool_1, return_1)

    def test_bake_chocolate_bar(self):
        """
        test bake_chocolate_bar functionality
        """
        # Params
        chocolate_choice = 'dark'
        m_raw_materials = self.selection['ingredients']
        d_raw_materials = {
            'sugar': 2,
            'butter': 2,
            'caramel': 15,
            'dark chocolate': 30,
            'mint chocolate': 30,
            'milk chocolate': 30,
            'light corn syrup': 2,
            'sweetened condensed milk': 2,
            'vanilla extract': 2,
            'Reese\'s Pieces': 15,
        }
        # Returns
        return_1 = 'A dark chocolate bar dispensed!'
        # Calls
        string_1 = self.chocolate_machine.bake_chocolate_bar(chocolate_choice, m_raw_materials, d_raw_materials)
        # Asserts
        self.assertEqual(string_1, return_1)


if __name__ == '__main__':
    unittest.main()
