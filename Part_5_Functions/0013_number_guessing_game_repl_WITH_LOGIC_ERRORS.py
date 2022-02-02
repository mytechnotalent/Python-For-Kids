from random import randint


def guess_number(f_guess, f_turns_left):
    """
    Functio to obtain player guess

    Params:
        f_guess: int
        f_turns_left: int

    Returns:
        int, str
    """
    try:
        if f_guess < 1 or f_guess > 9:
            raise ValueError
        return f_guess, f_turns_left - 1
    except ValueError:
        return '\nRULES: Please enter a number between 1 and 9.', f_turns_left - 1
    except TypeError:
        return '\nRULES: Please enter a number between 1 and 9.', f_turns_left - 1


def did_win(f_guess, f_correct_answer, f_turns_left):
    """
    Function to check player guess against the correct answer

    Params:
        f_guess: int
        f_correct_answer: int
        f_turns_left: int

    Returns:
        str, int, None
    """
    if f_turns_left >= 1:
        if f_guess > f_correct_answer:
            return 'HINT: Lower Than {0}'.format(f_guess), f_turns_left - 1
        elif f_guess < f_correct_answer:
            return 'HINT: Higher Than {0}'.format(f_guess), f_turns_left - 1
        else:
            return 'You won!', None


print('RULES: Guess a number between 1 and 9.')

correct_answer = randint(1, 9)
turns_left = 3
guess = 1

while guess != correct_answer:
    if turns_left >= 1:
        guess = input('Guess: ')
        guess_response, turns_left = guess_number(guess, turns_left)
        if turns_left > 1:
            print('{0} turns left.'.format(turns_left))
        elif turns_left == 1:
            print('{0} turn left.'.format(turns_left))
    else:
        print('The correct answer is {0}, let\'s play again!'.format(correct_answer))
        break

    if isinstance(guess_response, str):
        print(guess_response)
    else:
        if turns_left:
            game_status, turns_left = did_win(guess_response, correct_answer, turns_left)
            if game_status == 'You won!':
                print(game_status)
                break
            else:
                print(game_status)
