from microbit import display, Image, button_a, button_b, pin_logo, pin2

from grid import Grid
from game import Game
from escape_room_player import EscapeRoomPlayer

from config import *

grid = Grid(5, 5)
player = EscapeRoomPlayer('Mr. George')
game = Game()

game_on = True
while game_on:
    display.show(Image(grid.update(player)))
    
    player_move = True
    while player_move:
        if button_a.is_pressed():
            player.move_west(grid)
            player_move = False
        elif button_b.is_pressed():
            player.move_east(grid)
            player_move = False
        elif pin_logo.is_touched():
            player.move_north(grid)
            player_move = False
        elif pin2.is_touched():
            player.move_south(grid)
            player_move = False

    player_found_gold = game.generate_question(grid, player)
    player_response = None
    while player_found_gold:
        if button_a.is_pressed():
            player_response = 1
            did_player_win = game.did_player_win(grid, player, player_response)
            player_found_gold = False
            if did_player_win:
                game_on = False
        elif pin_logo.is_touched():
            player_response = 2
            did_player_win = game.did_player_win(grid, player, player_response)
            player_found_gold = False
            if did_player_win:
                game_on = False
        elif button_b.is_pressed():
            player_response = 3
            did_player_win = game.did_player_win(grid, player, player_response)
            player_found_gold = False
            if did_player_win:
                game_on = False
