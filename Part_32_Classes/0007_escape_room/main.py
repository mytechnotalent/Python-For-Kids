from time import sleep
from Grid import Grid
from EscapeRoomPlayer import EscapeRoomPlayer
from FileManager import FileManager
from Game import Game

grid = Grid(5, 5)
player = EscapeRoomPlayer()
file_manager = FileManager()
game = Game()

if __name__ == '__main__':
    player_location = None
    response = None
    final_question = False

    while True:
        # To ensure we do not generate a question if the player is hitting a wall
        # or not entering a valid move
        previous_player_location = player_location
        clear_screen, display_grid = game.update_ui(grid, player)
        print(clear_screen)
        print(display_grid)
        key = input('Enter A, D, W, S: ')
        if key == 'a':
            player_location = player.keyboard_a_press(grid)
        elif key == 'd':
            player_location = player.keyboard_d_press(grid)
        elif key == 'w':
            player_location = player.keyboard_w_press(grid)
        elif key == 's':
            player_location = player.keyboard_s_press(grid)
        else:
            pass
        random_location = (x, y) = game.generate_random_numbers(grid)
        if random_location == player_location and random_location != previous_player_location:
            random_question, answer_1, answer_2, answer_3, correct_answer_index, correct_answer \
                = game.ask_random_question()
            print(random_question)
            print('Press 1 for {0}.'.format(answer_1))
            print('Press 2 for {0}.'.format(answer_2))
            print('Press 3 for {0}.'.format(answer_3))
            while True:
                try:
                    response = int(input('ENTER: '))
                    break
                except ValueError:
                    print('Enter ONLY 1, 2 or 3!')
            if response == correct_answer_index + 1:
                print(game.correct_answer_response())
                inventory = player.get_inventory(file_manager)
                player.inventory.append(inventory)
                if 'Red Key' not in player.inventory and not final_question:
                    receive_red_key = game.generate_random_number(grid)
                    if receive_red_key == 2:
                        print(player.pick_up_red_key(file_manager))
                        final_question = True
                    else:
                        print(player.without_red_key())
                elif final_question:
                    print(game.win(file_manager))
                    sleep(3)
                    break
            else:
                print(game.incorrect_answer_response(correct_answer))
            sleep(3)
