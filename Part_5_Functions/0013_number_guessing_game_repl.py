from random import randint


def guess_number(f_guess, f_turns_left):
    """
    Function to obtain player guess

    Params:
        f_guess: str
        f_turns_left: int

    Returns:
        str, int
    """
    try:
        f_guess = int(f_guess)
        if f_guess < 1 or f_guess > 9:
            raise ValueError
        return f_guess, f_turns_left - 1
    except ValueError:
        return '\nRULES: Please enter a number between 1 and 9.', f_turns_left - 1
    except TypeError:
        return '\nRULES: Please enter a number between 1 and 9.', f_turns_left - 1


def did_win(f_guess, f_correct_answer):
    """
    Function to check player guess against the correct answer

    Params:
        f_guess: int, str
        f_correct_answer: int

    Returns:
        str
    """
    try:
        f_guess = int(f_guess)
        if f_guess > f_correct_answer:
            return 'HINT: Lower Than {0}'.format(f_guess)
        elif f_guess < f_correct_answer:
            return 'HINT: Higher Than {0}'.format(f_guess)
        else:
            return 'You won!'
    except ValueError:
        return '\nRULES: Please enter a number between 1 and 9.'
    except TypeError:
        return '\nRULES: Please enter a number between 1 and 9.'


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
