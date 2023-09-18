import consts
import random

def create_board():
    game_board = []

    for row in range(consts.BOARD_ROWS):
        game_rows = []
        for col in range(consts.BOARD_COLUMNS):
            game_rows.append(col)
        game_board.extend([game_rows])

    return game_board

def mines_on_board():
    mines_index = []
    count = 0

    while count < 20:
        bush_row_index = random.randint(0, 24)
        bush_column_index = random.randint(0, 49)
        bush = [bush_row_index, bush_column_index]
        if bush not in mines_index:
            mines_index.append(bush)
            count += 1

    return mines_index

def check_if_touching_flag(game_state):
    for row in range(game_state["soldier_state"]):
        if 21 <= row <= 22:
            for col in range(game_state["soldier_state"][row]):
                if 46 <= col <= 49:
                    return True


def check_if_touching_bomb(game_state):
    for i in range(len(game_state["soldier_state"])):
        if i == 3:
            for row in range(game_state["soldier_state"]):
                for col in range(game_state["soldier_state"][row]):
                    if create_board()[row][col] == consts.MINE_IMG:
                        return False
