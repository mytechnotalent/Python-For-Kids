from vending_machine import VendingMachine


class ChocolateMachine(VendingMachine):
    """
    Child class to represent a chocolate machine
    """

    def __init__(self, choices, __total_money_collected=0):
        """
        Params:
            choices: str
            __total_money_collected: float
        """
        self.choices = choices
        super().__init__()

    def stats(self, d_raw_materials=None):
        """
        Method to show machine statistics

        Params:
            d_raw_materials: dict

        Returns:
            str
        """
        cm_stats = 'sugar {0} tablespoons remaining\n'.format(d_raw_materials['sugar'])
        cm_stats += 'butter {0} teaspoons remaining\n'.format(d_raw_materials['butter'])
        cm_stats += 'dark chocolate {0} tablespoons remaining\n'.format(d_raw_materials['dark chocolate'])
        cm_stats += 'mint chocolate {0} tablespoons remaining\n'.format(d_raw_materials['mint chocolate'])
        cm_stats += 'milk chocolate {0} tablespoons remaining\n'.format(d_raw_materials['milk chocolate'])
        cm_stats += 'light corn syrup {0} teaspoons remaining\n'.format(d_raw_materials['light corn syrup'])
        cm_stats += 'sweetened condensed milk {0} teaspoons remaining\n'.format(d_raw_materials[
            'sweetened condensed milk'])
        cm_stats += 'vanilla extract {0} teaspoons remaining\n'.format(d_raw_materials['vanilla extract'])
        cm_stats += 'Reese\'s Pieces {0} tablespoons remaining\n'.format(d_raw_materials['Reese\'s Pieces'])
        cm_stats += super(ChocolateMachine, self).stats()
        return cm_stats

    def has_raw_materials(self, m_raw_materials, d_raw_materials):
        """
        Method to check if there are enough raw materials in the machine

        Params:
            m_raw_materials: dict
            d_raw_materials: dict

        Returns:
            str or bool
        """
        additional_resources_needed = ''
        for m_raw_material in m_raw_materials:
            if m_raw_materials[m_raw_material] > d_raw_materials[m_raw_material]:
                additional_resources_needed += 'Machine Needs Additional: {0}\n'.format(m_raw_material)
        if additional_resources_needed:
            return additional_resources_needed
        else:
            return True

    def bake_chocolate_bar(self, chocolate_choice, m_raw_materials, d_raw_materials):
        """
        Method to bake chocolate bar from raw materials

        Params:
            chocolate_choice: str
            m_raw_materials: dict

        Returns:
            str
        """
        for m_raw_material in m_raw_materials:
            d_raw_materials[m_raw_material] -= m_raw_materials[m_raw_material]
        return 'A {0} chocolate bar dispensed!'.format(chocolate_choice)
