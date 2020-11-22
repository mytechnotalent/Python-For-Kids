from microbit import *
	

	favorite_foods = ['pizza', 'ice cream', 'cookies']
	

	while True:
	    display.scroll(
	                   'I love to eat ' +
	                   favorite_foods[0] + ', ' +
	                   favorite_foods[1] + ', ' +
	                   'and ' +
	                   favorite_foods[2] + '!'
	                  )