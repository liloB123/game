import consts

def create_board():
    game_board = []

    for row in range(len(consts.NUM_OF_ROWS)):
        game_rows = []
        for col in range(len(consts.NUM_OF_COLS)):
            game_rows.append(col)
        game_board.extend([game_rows])

    return game_board
