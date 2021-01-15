CHOCOLATE_CHOICES = {
    'dark': {
        'ingredients': {
            'sugar': 1,
            'butter': 1,
            'dark chocolate': 6,
            'light corn syrup': 1,
            'sweetened condensed milk': 1,
            'vanilla extract': 1,
        },
        'price': 2.75,
    },
    'mint': {
        'ingredients': {
            'sugar': 1,
            'butter': 1,
            'mint chocolate': 6,
            'light corn syrup': 1,
            'sweetened condensed milk': 1,
            'vanilla extract': 1,
        },
        'price': 2.50,
    },
    'caramel': {
        'ingredients': {
            'sugar': 1,
            'caramel': 3,
            'butter': 1,
            'milk chocolate': 6,
            'light corn syrup': 1,
            'sweetened condensed milk': 1,
            'vanilla extract': 1,
        },
        'price': 3.25,
    },
    'surprise': {
        'ingredients': {
            'sugar': 1,
            'Reese\'s Pieces': 3,
            'butter': 1,
            'milk chocolate': 6,
            'light corn syrup': 1,
            'sweetened condensed milk': 1,
            'vanilla extract': 1,
        },
        'price': 3.25,
    },
}

raw_materials = {
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

total_money_collected = 0
SHUTDOWN_PASSWORD = '8675309'


def has_raw_materials(f_raw_materials):
    """Check if there are enough raw materials in the machine

    Params:
        f_raw_materials: dict

    Returns:
        str or True
    """
    additional_resources_needed = ''
    for f_raw_material in f_raw_materials:
        if f_raw_materials[f_raw_material] > raw_materials[f_raw_material]:
            additional_resources_needed += 'Machine Needs Additional: {0}\n'.format(f_raw_material)
    if additional_resources_needed:
        return additional_resources_needed
    else:
        return True


def collect_money(f_max_value, m_quarters, m_dimes, m_nickels):
    """Collect money into the machine

    Params:
        f_max_value: float

    Returns:
        float or str
    """
    try:
        money_collected = int(m_quarters) * 0.25
        money_collected += int(m_dimes) * 0.10
        money_collected += int(m_nickels) * 0.05
        if money_collected <= 0.00:
            return 'Insufficient funds...  Dispensing coins inserted.'
        elif money_collected >= f_max_value:
            return 'Machine can\'t hold more than ${0:.2f}...  Dispensing coins inserted.'.format(f_max_value)
        else:
            return money_collected
    except ValueError:
        return 'Please enter valid currency...  Dispensing any coins inserted.\n'


def has_enough_money(f_money_collected, f_chocolate_price):
    """Check to see if customer put in enough money into the machine

    Params:
        f_money_collected: float
        f_chocolate_price: float

    Returns:
        str
    """
    if f_money_collected >= f_chocolate_price:
        excess_money_collected = round(f_money_collected - f_chocolate_price, 2)
        global total_money_collected
        total_money_collected += f_chocolate_price
        return 'Change: ${0:.2f}\n'.format(excess_money_collected)
    else:
        return 'Insufficient funds...  Dispensing coins inserted.\n'


def bake_chocolate_bar(f_chocolate_choice, f_raw_materials):
    """Bake chocolate bar from raw materials

    Params:
        f_chocolate_choice: str
        f_raw_materials: dict

    Returns:
        str
    """
    for f_raw_material in f_raw_materials:
        raw_materials[f_raw_material] -= f_raw_materials[f_raw_material]
    return 'A {0} chocolate bar dispensed!'.format(f_chocolate_choice)


def stats():
    """
    Show machine statistics

    Returns:
        str
    """
    cm_stats = 'sugar {0} tablespoons remaining\n'.format(raw_materials['sugar'])
    cm_stats += 'butter {0} teaspoons remaining\n'.format(raw_materials['butter'])
    cm_stats += 'dark chocolate {0} tablespoons remaining\n'.format(raw_materials['dark chocolate'])
    cm_stats += 'mint chocolate {0} tablespoons remaining\n'.format(raw_materials['mint chocolate'])
    cm_stats += 'milk chocolate {0} tablespoons remaining\n'.format(raw_materials['milk chocolate'])
    cm_stats += 'light corn syrup {0} teaspoons remaining\n'.format(raw_materials['light corn syrup'])
    cm_stats += 'sweetened condensed milk {0} teaspoons remaining\n'.format(raw_materials[
        'sweetened condensed milk'])
    cm_stats += 'vanilla extract {0} teaspoons remaining\n'.format(raw_materials['vanilla extract'])
    cm_stats += 'Reese\'s Pieces {0} tablespoons remaining\n'.format(raw_materials['Reese\'s Pieces'])
    cm_stats += 'Total Money Collected: ${0:.2f}\n'.format(total_money_collected)
    return cm_stats


machine_active = True
choices = ['dark', 'caramel', 'mint', 'surprise', 'stats', 'shutdown']

while machine_active:
    valid_choice = False
    choice = input('ORDER [dark - caramel - mint - surprise]: ')
    if choice in choices:
        valid_choice = True
    else:
        print('That is not a valid selection...\n')
    if choice == 'shutdown':
        entered_password = input('ENTER SHUTDOWN PASSWORD: ')
        if entered_password == SHUTDOWN_PASSWORD:
            machine_active = False
        else:
            print('YOU ARE NOT AUTHORIZED TO DISABLE THIS MACHINE!\n')
    elif choice == 'stats':
        stats_ = stats()
        print(stats_)
    elif valid_choice:
        selection = CHOCOLATE_CHOICES[choice]
        has_enough_raw_materials = has_raw_materials(selection['ingredients'])
        if not isinstance(has_enough_raw_materials, bool):
            print(has_enough_raw_materials)
            machine_active = False
        if isinstance(has_enough_raw_materials, bool):
            quarters = input('Quarters: ')
            dimes = input('Dimes: ')
            nickels = input('Nickels: ')
            money = collect_money(100.00, quarters, dimes, nickels)
            if not isinstance(money, float):
                print(money)
            else:
                change = has_enough_money(money, selection['price'])
                if change == 'Insufficient funds...  Dispensing coins inserted.\n':
                    print(change)
                else:
                    chocolate_bar = bake_chocolate_bar(choice, selection['ingredients'])
                    print(chocolate_bar)
                    print(change)
        else:
            machine_active = False

print('We are going down for maintenance...')
