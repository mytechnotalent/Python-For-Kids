from random import randint
from funcs import guess_number, did_win

print('RULES: Guess a number between 1 and 9.')

correct_answer = randint(1, 9)
turns_left = 3
guess = 0

while guess != correct_answer:
    if turns_left >= 0:
        guess = input('Guess: ')
        guess, turns_left = guess_number(guess, turns_left)
        if guess != correct_answer:
            if turns_left > 1:
                print('{0} turns left.'.format(turns_left))
            elif turns_left == 1:
                print('{0} turn left.'.format(turns_left))
            else:
                print('The correct answer is {0}, let\'s play again!'.format(correct_answer))
                break
        game_status = did_win(guess, correct_answer)
        if game_status == 'You won!':
            print(game_status)
            break
        else:
            print(game_status)
