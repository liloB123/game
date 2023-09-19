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
    for index in mines_list:
        index_x_mine = math.ceil(index[0] / consts.SQUARE_SIZE)
        index_y_mine = math.ceil(index[1] / consts.SQUARE_SIZE)
        count = -1
        for i in state["soldier_state"]:
            count += 1
            if count > 5:
                for h in range(3):
                    if i[0] == index_y_mine and i[1] == index_x_mine + h:
                        return True



def flag_on_board(state):
    flag_x = consts.WINDOW_WIDTH - 4 * consts.SQUARE_SIZE
    flag_y = consts.WINDOW_HEIGHT - 3 * consts.SQUARE_SIZE
    index_x_flag = math.ceil(flag_x / consts.SQUARE_SIZE)
    index_y_flag = math.ceil(flag_y / consts.SQUARE_SIZE)
    count = -1
    for i in state["soldier_state"]:
        count += 1
        if count < 6:
            for h in range(3):
                for k in range(4):
                    if i[0] == index_y_flag + h and i[1] == index_x_flag + k:
                         return True


