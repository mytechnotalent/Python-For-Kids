from microbit import display, Image
from speech import say

SPEED = 95

display.show(Image.SURPRISED)
say('Hello World!', speed=SPEED)
display.show(Image.HAPPY)
