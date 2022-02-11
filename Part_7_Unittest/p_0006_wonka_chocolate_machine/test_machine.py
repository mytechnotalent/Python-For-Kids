import unittest

from machine import Machine


class TestMachine(unittest.TestCase):
    """
    Test class to test machine module
    """
    
    def setUp(self):
        """
        setUp class
        """
        # Instantiate
        self.machine = Machine()

    def test_stats(self):
        """
        test stats functionality
        """
        # Returns
        return_1 = 'Total Money Collected: $0.00\n'
        
        # Calls
        string_1 = self.machine.stats()
        
        # Asserts
        self.assertEqual(string_1, return_1)

    def test_collect_money(self):
        """
        test collect_money functionality
        """
        # Params
        max_value = 100.00
        m_quarters = 2
        m_dimes = 2
        m_nickels = 1
        
        # Returns
        return_1 = 0.75
        
        # Calls
        float_1 = self.machine.collect_money(max_value, m_quarters, m_dimes, m_nickels)
        
        # Asserts
        self.assertEqual(float_1, return_1)

    def test_collect_money_handles_overflow_of_money_collected(self):
        """
        test collect_money functionality handles overflow of money collected
        """
        # Params
        max_value = 100.00
        m_quarters = 2000
        m_dimes = 2
        m_nickels = 1
        
        # Returns
        return_1 = 'Machine can\'t hold more than $100.00...  Dispensing coins inserted.\n'
        
        # Calls
        string_1 = self.machine.collect_money(max_value, m_quarters, m_dimes, m_nickels)
        
        # Asserts
        self.assertEqual(string_1, return_1)

    def test_collect_money_handles_invalid_currency(self):
        """
        test collect_money functionality handles invalid currency
        """
        # Params
        max_value = 100.00
        m_quarters = 'invalid data'
        m_dimes = 2
        m_nickels = 1
        
        # Returns
        return_1 = 'Please enter valid currency...  Dispensing any coins inserted.\n'
        
        # Calls
        string_1 = self.machine.collect_money(max_value, m_quarters, m_dimes, m_nickels)
        
        # Asserts
        self.assertEqual(string_1, return_1)

    def test_has_enough_money(self):
        """
        test has_enough_money functionality
        """
        # Params
        price = 2.50
        self.__total_money_collected = 10.00
        __money_collected = 6.00
        
        # Returns
        return_1 = 'Change: $3.50\n'
        
        # Calls
        string_1 = self.machine.has_enough_money(price, __money_collected)
        
        # Asserts
        self.assertEqual(string_1, return_1)

    def test_has_enough_money_handles_insufficient_funds(self):
        """
        test has_enough_money functionality handles insufficient funds
        """
        # Params
        price = 2.50
        self.__total_money_collected = 10.00
        __money_collected = 1.00
        
        # Returns
        return_1 = 'Insufficient funds...  Dispensing coins inserted.\n'
        
        # Calls
        string_1 = self.machine.has_enough_money(price, __money_collected)
        
        # Asserts
        self.assertEqual(string_1, return_1)

    def test_shutdown_machine(self):
        """
        test shutdown_machine
        """
        # Params
        shutdown_password = '8675309'
        entered_password = '8675309'
        
        # Returns
        return_1 = None
        
        # Calls
        none_1 = self.machine.shutdown_machine(shutdown_password, entered_password)
        
        # Asserts
        self.assertEqual(none_1, return_1)

    def test_shutdown_machine_handles_incorrect_password(self):
        """
        test shutdown_machine handles incorrect password
        """
        # Params
        shutdown_password = '8675309'
        entered_password = 'not_correct_password'
        
        # Returns
        return_1 = 'YOU ARE NOT AUTHORIZED TO DISABLE THIS MACHINE!\n'
        
        # Calls
        string_1 = self.machine.shutdown_machine(shutdown_password, entered_password)
        
        # Asserts
        self.assertEqual(string_1, return_1)


if __name__ == '__main__':
    unittest.main()
