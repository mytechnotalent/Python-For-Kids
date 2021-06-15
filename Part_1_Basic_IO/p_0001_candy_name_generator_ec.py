from microbit import display, Image
from speech import say

SPEED = 95

candy_title = input('What is the candy title? ')
candy_flavor = input('What is the candy flavor? ')

display.show(Image.SURPRISED)
print('It shall be called {0} {1}!'.format(candy_title, candy_flavor))
say('It shall be called {0} {1}!'.format(candy_title, candy_flavor))
display.show(Image.HAPPY)
