from chocolate_machine import ChocolateMachine
from data import CHOCOLATE_CHOICES, raw_materials
from config import *

chocolate_machine = ChocolateMachine(CHOICES)

chocolate_machine_active = True
while chocolate_machine_active:
    valid_choice = False
    choice = input('ORDER [dark @ $2.75 - caramel @ $3.25 - mint @ $2.50 - surprise @ $3.25]: ')
    if choice in CHOICES:
        valid_choice = True
    else:
        print('That is not a valid selection...\n')
    if choice == 'shutdown':
        entered_password = input('ENTER SHUTDOWN PASSWORD: ')
        not_authorized = chocolate_machine.shutdown_machine('8675309', entered_password)
        if not_authorized:
            print(not_authorized)
        else:
            chocolate_machine_active = False
    elif choice == 'stats':
        stats = chocolate_machine.stats(raw_materials)
        print(stats)
    elif valid_choice:
        selection = CHOCOLATE_CHOICES[choice]
        has_enough_raw_materials = chocolate_machine.has_raw_materials(selection['ingredients'], raw_materials)
        if not isinstance(has_enough_raw_materials, bool):
            print(has_enough_raw_materials)
            chocolate_machine_active = False
        if isinstance(has_enough_raw_materials, bool):
            quarters = input('Quarters: ')
            dimes = input('Dimes: ')
            nickels = input('Nickels: ')
            money_collected = chocolate_machine.collect_money(MAX_VALUE, quarters, dimes, nickels)
            if not isinstance(money_collected, float):
                print(money_collected)
            else:
                change = chocolate_machine.has_enough_money(selection['price'])
                if change == 'Insufficient funds...  Dispensing coins inserted.\n':
                    print(change)
                else:
                    chocolate_bar = chocolate_machine.bake_chocolate_bar(choice, selection['ingredients'],
                                                                         raw_materials)
                    print(chocolate_bar)
                    print(change)
    elif valid_choice:
        chocolate_machine_active = False

print('We are going down for maintenance...')
