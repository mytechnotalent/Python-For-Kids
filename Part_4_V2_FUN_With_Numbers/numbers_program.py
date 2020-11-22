from microbit import *


counter = 0


while True:
    if button_a.was_pressed():
        counter = counter + 1
        display.scroll(str(counter))
    if button_b.was_pressed():
        counter = counter - 1
        display.scroll(str(counter))