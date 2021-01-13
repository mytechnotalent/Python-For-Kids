from random import randint

random_number = randint(1, 2)

choice = input('Enter A - Heads OR B - Tails: ').lower()
if random_number == 1 and choice == 'a':
    print('You WON!')
elif random_number == 1 and choice == 'b':
    print('You Lost')
elif random_number == 2 and choice == 'b':
    print('You Won!')
else:
    print('You Lost')