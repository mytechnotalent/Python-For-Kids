class Machine:
    """
    Base class to represent a generic vending machine
    """

    def __init__(self):
        """
        Attrs:
            self.__money_collected: float
            self.__total_money_collected: float
            self.__price: float
        """
        self.__money_collected = 0
        self.__total_money_collected = 0
        self.__price = 0

    def stats(self):
        """
        Show machine statistics

        Returns:
            str
        """
        return 'Total Money Collected: ${0:.2f}\n'.format(self.__total_money_collected)

    def collect_money(self, max_value, m_quarters, m_dimes, m_nickels):
        """
        Collects money into machine

        Params:
            max_value: float

        Returns:
            float or str
        """
        try:
            self.__money_collected = int(m_quarters) * 0.25
            self.__money_collected += int(m_dimes) * 0.10
            self.__money_collected += int(m_nickels) * 0.05
            if self.__money_collected <= 0.00:
                return 'Please enter coins...\n'
            elif self.__money_collected >= max_value:
                return 'Machine can\'t hold more than ${0:.2f}...  Dispensing coins inserted.\n'.format(max_value)
            else:
                return self.__money_collected
        except ValueError:
            return 'Please enter valid currency...  Dispensing any coins inserted.\n'

    def has_enough_money(self, price):
        """Check to see if customer put in enough money into the machine

        Params:
            price: float

        Returns:
            str
        """
        excess_money_collected = round(self.__money_collected - price, 2)
        if self.__money_collected >= price:
            self.__total_money_collected += price
            return 'Change: ${0:.2f}\n'.format(excess_money_collected)
        else:
            return 'Insufficient funds...  Dispensing coins inserted.\n'.format(excess_money_collected)

    @staticmethod
    def shutdown_machine(shutdown_password, entered_password):
        """Shutdown machine

        Params:
            shutdown_password: str
            entered_password: str

        Returns:
            str
        """
        if entered_password != shutdown_password:
            return 'YOU ARE NOT AUTHORIZED TO DISABLE THIS MACHINE!\n'
