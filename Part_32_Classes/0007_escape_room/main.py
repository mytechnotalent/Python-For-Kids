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
    question_1 = False
    final_question = False

    while True:
        game.update_ui(grid, player)
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
            player_location = 1, 1

        x, y = game.generate_random_numbers(grid)
        if player_location == (x, y) and not question_1:
            player.get_inventory(file_manager)
            if 'Red Key' not in player.inventory:
                response, correct_answer_index, correct_answer = game.ask_question()
                if response == correct_answer_index:
                    correct = game.correct_answer_response()
                    print(correct)
                    picked_up_red_key = player.pick_up_red_key(file_manager)
                    print(picked_up_red_key)
                    question_1 = True
                    sleep(3)
                else:
                    game.incorrect_answer_response(correct_answer)

        x, y = game.generate_random_numbers(grid)
        if player_location == (x, y) and not final_question:
            player.get_inventory(file_manager)
            response, correct_answer_index, correct_answer = game.ask_question()
            if response == correct_answer_index:
                correct = game.correct_answer_response()
                print(correct)
                final_question = True
                sleep(3)
            else:
                correct_answer = game.incorrect_answer_response(correct_answer)
                print(correct_answer)
            if 'Red Key' in player.inventory and final_question:
                win = game.win(file_manager)
                print(win)
                break
            elif final_question:
                without_red_key = player.without_red_key()
                print(without_red_key)
                sleep(3)
