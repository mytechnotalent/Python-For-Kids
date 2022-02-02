import unittest

from ..funcs import has_raw_materials, collect_money, has_enough_money, bake_chocolate_bar, stats
from ..data import CHOCOLATE_CHOICES


class TestFuncs(unittest.TestCase):
    """
    Test class to test funcs module
    """
    
    def test_has_raw_materials(self):
        """
        test has_raw_materials functionality
        """
        # Setup
        choice = 'dark'
        selection = CHOCOLATE_CHOICES[choice]
        # Params
        f_raw_materials = selection['ingredients']
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
        bool_1 = has_raw_materials(f_raw_materials, d_raw_materials)
        # Asserts
        self.assertEqual(bool_1, return_1)

    def test_has_raw_materials_handles_insufficient_raw_materials(self):
        """
        test has_raw_materials handles insufficient raw materials functionality
        """
        # Setup
        choice = 'dark'
        selection = CHOCOLATE_CHOICES[choice]
        # Params
        f_raw_materials = selection['ingredients']
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
        string_1 = has_raw_materials(f_raw_materials, d_raw_materials)
        # Asserts
        self.assertEqual(string_1, return_1)

    def test_collect_money(self):
        """
        test collect_money functionality
        """
        # Params
        f_max_value = 100.00
        f_quarters = 22
        f_dimes = 10
        f_nickels = 5
        # Returns
        return_1 = 6.75
        # Calls
        float_1 = collect_money(f_max_value, f_quarters, f_dimes, f_nickels)
        # Asserts
        self.assertEqual(float_1, return_1)

    def test_collect_money_handles_excess_funds_over_max_value(self):
        """
        test collect_money handles excess funds over max value functionality
        """
        # Params
        f_max_value = 100.00
        f_quarters = 2000
        f_dimes = 1
        f_nickels = 5
        # Returns
        return_1 = 'Machine can\'t hold more than $100.00...  Dispensing coins inserted.'
        # Calls
        string_1 = collect_money(f_max_value, f_quarters, f_dimes, f_nickels)
        # Asserts
        self.assertEqual(string_1, return_1)

    def test_collect_money_handles_value_error(self):
        """
        test collect_money handles value error functionality
        """
        # Params
        f_max_value = 100.00
        f_quarters = 'k'
        f_dimes = 1
        f_nickels = 5
        # Returns
        return_1 = 'Please enter valid currency.\n'
        # Calls
        string_1 = collect_money(f_max_value, f_quarters, f_dimes, f_nickels)
        # Asserts
        self.assertEqual(string_1, return_1)

    def test_has_enough_money(self):
        """
        test has_enough_money functionality
        """
        # Params
        f_money_collected = 2.50
        f_chocolate_price = 2.25
        f_total_money_collected = 2.25
        # Returns
        return_1 = 'Change: $0.25\n', 4.5
        # Calls
        string_1 = has_enough_money(f_money_collected, f_chocolate_price, f_total_money_collected)
        # Asserts
        self.assertEqual(string_1, return_1)

    def test_has_enough_money_handles_insufficient_funds(self):
        """
        test has_enough_money handles insufficient funds functionality
        """
        # Params
        f_money_collected = 2.00
        f_chocolate_price = 2.25
        f_total_money_collected = 2.25
        # Returns
        return_1 = 'Insufficient funds...  Dispensing coins inserted.\n'
        # Calls
        string_1 = has_enough_money(f_money_collected, f_chocolate_price, f_total_money_collected)
        # Asserts
        self.assertEqual(string_1, return_1)

    def test_bake_chocolate_bar(self):
        """
        test bake_chocolate_bar functionality
        """
        # Setup
        choice = 'dark'
        selection = CHOCOLATE_CHOICES[choice]
        # Params
        f_chocolate_choice = 'dark'
        f_raw_materials = selection['ingredients']
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
        string_1 = bake_chocolate_bar(f_chocolate_choice, f_raw_materials, d_raw_materials)
        # Asserts
        self.assertEqual(string_1, return_1)

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
        f_money_collected = 0.00
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
        string_1 = stats(d_raw_materials, f_money_collected)
        # Asserts
        self.assertEqual(string_1, return_1)


if __name__ == '__main__':
    unittest.main()
