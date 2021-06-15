from random import randint
from microbit import display, Image, button_a, button_b, pin_logo
from speech import say

SPEED = 95

random_number = randint(1, 9)

# Create number_position and init to 1
number_position = 1

display.show(Image.SURPRISED)
say('Pick a number between 1 and 9.', speed=SPEED)
display.show(Image.HAPPY)

while True:
    display.show(number_position)
    
    if button_a.was_pressed():
        if number_position == 9:
            pass
        else:
            number_position += 1
            display.show(number_position)
            
    if button_b.was_pressed():
        if number_position == 1:
            pass
        else:
            number_position -= 1
            display.show(number_position)
     
    if pin_logo.is_touched():
        if number_position == random_number:
            display.show(Image.SURPRISED)
            say('Correct!', speed=SPEED)
            display.show(Image.HAPPY)
            break
        else:
            display.show(Image.SURPRISED)
            say('The number I chose is {0}.'.format(random_number), speed=SPEED)
            display.show(Image.HAPPY)
            break
