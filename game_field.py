import black_screen
import consts
import random
import math

def create_board():
    game_board = []

    for row in range(consts.BOARD_ROWS):
        game_rows = []
        for col in range(consts.BOARD_COLUMNS):
            game_rows.append(col)
        game_board.extend([game_rows])

    return game_board

def mines_on_board(state):
    mines_list = black_screen.mines_places
    x = state["soldier_state"]
    for index in mines_list:
        index_x_mine = math.ceil(index[0] / consts.SQUARE_SIZE)
        index_y_mine = math.ceil(index[1] / consts.SQUARE_SIZE)
        for i in range(len(state["soldier_state"])):
            if i > 5:
                if state["soldier_state"][i][0] == index_y_mine and state["soldier_state"][i][1] == index_x_mine:
                    state["state"] = consts.LOSE_STATE


def check_if_touching_flag(game_state):
    for row in range(game_state["soldier_state"]):
        if 21 <= row <= 22:
            for col in range(game_state["soldier_state"][row]):
                if 46 <= col <= 49:
                    return True


def check_if_touching_mine(game_state):
    for i in range(len(game_state["soldier_state"])):
        if i == 3:
            for row in range(game_state["soldier_state"]):
                for col in range(game_state["soldier_state"][row]):
                    if create_board()[row][col] == consts.MINE_IMG:
                        return False
