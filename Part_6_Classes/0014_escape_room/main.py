from microbit import display, Image, button_a, button_b, pin_logo, pin2
from grid import Grid
from escape_room_player import EscapeRoomPlayer
from data import questions
from file_manager import FileManager
from game import Game
from speech import say
import music

grid = Grid(5, 5)
player = EscapeRoomPlayer()
file_manager = FileManager()
game = Game()

player_location = None
response = None
final_question = False
SPEED = 95

previous_player_location = player_location
update_grid = grid.update(player)

while True:
    # To ensure we do not generate a question if the player is hitting a wall
    # or not entering a valid move
    previous_player_location = player_location
    display.show(Image(update_grid))
    while True:
        if button_a.is_pressed():
            player_location = player.move_west(grid)
            update_grid = grid.update(player)
            break
        elif button_b.is_pressed():
            player_location = player.move_east(grid)
            update_grid = grid.update(player)
            break
        elif pin_logo.is_touched():
            player_location = player.move_north(grid)
            update_grid = grid.update(player)
            break
        elif pin2.is_touched():
            player_location = player.move_south(grid)
            update_grid = grid.update(player)
            break
    random_location = (x, y) = game.generate_random_numbers(grid)
    if random_location == player_location and random_location != previous_player_location:
        random_question, answer_1, answer_2, answer_3, correct_answer_index, correct_answer \
            = game.ask_random_question(questions)
        display.show(Image.SURPRISED)
        say(random_question, speed=SPEED)
        say('Press the aay button for {0}.'.format(answer_1), speed=SPEED)
        say('Press the logo for {0}.'.format(answer_2), speed=SPEED)
        say('Press the bee button for {0}.'.format(answer_3), speed=SPEED)
        display.show(Image.HAPPY)
        while True:
            if button_a.is_pressed():
                response = 1
                break
            elif pin_logo.is_touched():
                response = 2
                break
            elif button_b.is_pressed():
                response = 3
                break
        if response == correct_answer_index + 1:
            display.show(Image.SURPRISED)
            say(game.correct_answer_response(), speed=SPEED)
            inventory = player.get_inventory(file_manager)
            player.inventory.append(inventory)
            if 'Red Key' in player.inventory:
                final_question = True
            if 'Red Key' not in player.inventory and not final_question:
                receive_red_key = game.generate_random_number(grid)
                if receive_red_key == 2:
                    display.show(Image.SURPRISED)
                    say(player.pick_up_red_key(file_manager), speed=SPEED)
                    final_question = True
                else:
                    display.show(Image.SURPRISED)
                    say(player.without_red_key(), speed=SPEED)
            elif final_question:
                display.show(Image.SURPRISED)
                say(game.win(file_manager), speed=SPEED)
                music.play(music.POWER_UP)
                display.show(Image.ALL_CLOCKS, loop=False, delay=100)
                break
        else:
            display.show(Image.SURPRISED)
            say(game.incorrect_answer_response(correct_answer), speed=SPEED)
