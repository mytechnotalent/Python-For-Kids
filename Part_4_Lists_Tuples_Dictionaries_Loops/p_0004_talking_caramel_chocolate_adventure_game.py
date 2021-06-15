from random import choice
from microbit import display, Image, button_a, button_b, pin_logo
from speech import say
from time import sleep

SPEED = 95

chocolates = ['milk', 'white', 'dark', 'caramel', 'mint']
rooms = {}
room_number = 1
guesses = 2

for room in range(1, len(chocolates) + 1):
    random_chocolate = choice(chocolates)
    rooms[room] = random_chocolate
    chocolates.remove(random_chocolate)
    
display.show(Image.SURPRISED)
say('Welcome to the Talking Caramel Chocolate Adventure Game!', speed=SPEED)
display.show(Image.HAPPY)
sleep(1)
display.show(Image.SURPRISED)
say('Press the A and B buttons to move back and fourth through 5 ', speed=SPEED)
say('different rooms as your goal find the room with the caramel ', speed=SPEED)
say('chocolate.', speed=SPEED)
display.show(Image.HAPPY)
sleep(1)
display.show(Image.SURPRISED)
say('You get two guesses.', speed=SPEED)
display.show(Image.HAPPY)
sleep(1)
display.show(Image.SURPRISED)
say('If you press the logo and if the caramel chocolate ', speed=SPEED)
say('is in that room you win!', speed=SPEED)
display.show(Image.HAPPY)
sleep(1)
display.show(Image.SURPRISED)
say('Let the games begin!', speed=SPEED)
display.show(Image.HAPPY)
sleep(1)
 
while guesses > 0:
    display.show(room_number)
    if button_a.was_pressed():
        if room_number == 5:
            pass
        else:
            room_number += 1
            display.show(room_number)   
    if button_b.was_pressed():
        if room_number == 1:
            pass
        else:
            room_number -= 1
            display.show(room_number)
    if pin_logo.is_touched():
        if rooms[room_number] == 'caramel':
            display.show(Image.SURPRISED)
            say('You found the caramel chocolate!  Great job!', speed=SPEED)
            display.show(Image.HAPPY)
            break
        else:
            display.show(Image.SURPRISED)
            say('Sorry this room has {0} chocolate.'.format(rooms[room_number]), speed=SPEED)
            display.show(Image.HAPPY)
            sleep(1)
            guesses -= 1
            
if guesses <= 0:
    display.show(Image.SURPRISED)
    say('Sorry about that.  Please try again by click the reset button.', speed=SPEED)
    display.show(Image.HAPPY)
    sleep(1)
else:
    display.show(Image.SURPRISED)
    say('Click the reset button to play again.', speed=SPEED)
    display.show(Image.HAPPY)
    sleep(1)

