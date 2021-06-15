from microbit import display, Image
from speech import say

SPEED = 95

player_score = int(input('Enter Player Score: '))
player_score_bonus = int(input('Enter Player Score Bonus: '))
player_has_golden_ticket = True

player_final_score = player_score + player_score_bonus

display.show(Image.SURPRISED)
print('Player final score is {0} and has golden ticket is {1}.'.format(player_final_score, player_has_golden_ticket))
say('Player final score is {0} and has golden ticket is {1}.'.format(player_final_score, player_has_golden_ticket))
display.show(Image.HAPPY)