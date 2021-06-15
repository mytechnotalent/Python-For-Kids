from microbit import display, Image
from speech import say

SPEED = 95

noun = input('Enter Noun: ')
verb = input('Enter Verb: ')
miles = int(input('Enter Miles: '))

display.show(Image.SURPRISED)
print('My {0} are {1}!'.format(noun, verb))
say('My {0} are {1}!'.format(noun, verb))
print('It traveled {0} miles!'.format(miles))
say('It traveled {0} miles!'.format(miles))
display.show(Image.HAPPY)
