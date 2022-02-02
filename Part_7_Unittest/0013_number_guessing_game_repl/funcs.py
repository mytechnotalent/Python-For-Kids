def guess_number(f_guess, f_turns_left):
    """
    Function to obtain player guess

    Params:
        f_guess: str
        f_turns_left: int

    Returns:
        int, int or str, int
    """
    try:
        f_guess = int(f_guess)
        if f_guess < 1 or f_guess > 9:
            raise ValueError
        return f_guess, f_turns_left - 1
    except ValueError:
        return '\nRULES: Please enter a number between 1 and 9.', f_turns_left - 1


def did_win(f_guess, f_correct_answer):
    """
    Function to check player guess against the correct answer

    Params:
        f_guess: int or str
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
