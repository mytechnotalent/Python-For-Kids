from random import randint

turns_left = 3


def guess_number():
    """Obtain player guess

    Returns:
        int or False
    """
    try:
        f_guess = int(input('Guess: '))
        if f_guess < 1 or f_guess > 9:
            raise ValueError
        return f_guess
    except ValueError:
        print('\nRULES: Please enter a number between 1 and 9.')
        return False


def did_win(f_guess, f_correct_answer, f_turns_left):
    """Check player guess against the correct answer

    Args:
        f_guess: int
        f_correct_answer: int
        f_turns_left: int

    Returns:
        int or False
    """
    if f_turns_left > 1:
        if f_guess > f_correct_answer:
            print('HINT: Lower Than {0}'.format(f_guess))
            return f_turns_left - 1
        elif f_guess < f_correct_answer:
            print('HINT: Higher Than {0}'.format(f_guess))
            return f_turns_left - 1
        else:
            print('You won!')
            return False
    else:
        return False


print('RULES: Guess a number between 1 and 9.')

correct_answer = randint(1, 9)

guess = 0

while guess != correct_answer:
    guess = guess_number()

    if guess:
        turns_left = did_win(guess, correct_answer, turns_left)

    if turns_left == 0:
        print('The correct answer is {0}, let\'s play again!'.format(correct_answer))
        break

    if guess and turns_left:
        print('{0} turns left.\n'.format(turns_left))
