from random import randint
from microbit import display, button_a, button_b

display.scroll('Heads = A')
display.scroll('Tails = B')
random_number = randint(1, 2)

while True:
    if button_a.is_pressed():
        if random_number == 1:
            display.scroll('You WON!')
            break
        else:
            display.scroll('You Lost')
            break
        
    if button_b.is_pressed():
        if random_number == 2:
            display.scroll('You WON!')
            break
        else:
            display.scroll('You Lost')
            break