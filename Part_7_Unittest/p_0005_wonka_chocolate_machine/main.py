from funcs import has_raw_materials, collect_money, has_enough_money, bake_chocolate_bar, stats
from data import CHOCOLATE_CHOICES, raw_materials

CHOICES = ('dark', 'caramel', 'mint', 'surprise', 'stats', 'shutdown')
SHUTDOWN_PASSWORD = '8675309'
total_money_collected = 0

machine_active = True
while machine_active:
    valid_choice = False
    choice = input('ORDER [dark - caramel - mint - surprise]: ')
    if choice in CHOICES:
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
        stats_ = stats(raw_materials, total_money_collected)
        print(stats_)
    elif valid_choice:
        selection = CHOCOLATE_CHOICES[choice]
        has_enough_raw_materials = has_raw_materials(selection['ingredients'], raw_materials)
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
                change = has_enough_money(money, selection['price'], total_money_collected)
                if change == 'Insufficient funds...  Dispensing coins inserted.\n':
                    print(change)
                else:
                    chocolate_bar = bake_chocolate_bar(choice, selection['ingredients'], raw_materials)
                    print(chocolate_bar)
                    print(change)
        else:
            machine_active = False

print('We are going down for maintenance...')
