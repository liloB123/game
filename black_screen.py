import pygame
import consts
import random



black_board = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def print_black_screen(state):
    black_board.fill(consts.BLACK_COLOR)
    for x in range(0, consts.WINDOW_WIDTH, consts.SQUARE_SIZE):
        for y in range(0, consts.WINDOW_HEIGHT, consts.SQUARE_SIZE):
            rect = pygame.Rect(x, y, consts.SQUARE_SIZE, consts.SQUARE_SIZE)
            pygame.draw.rect(black_board, consts.GRID_GREEN_COLOR, rect, 1)

    put_mines_on_screen(mines_places)
    night_soldier(state["soldier_pic_loc_x"], state["soldier_pic_loc_y"])
    pygame.display.flip()

def random_mines_place():
    mines_index_list = []
    count = 0
    while count < 20:
        mine_x = random.randint(0, (consts.BOARD_COLUMNS * consts.SQUARE_SIZE - consts.SQUARE_SIZE))
        mine_y = random.randint(0, (consts.BOARD_ROWS * consts.SQUARE_SIZE - consts.SQUARE_SIZE))
        mine_index = [mine_x, mine_y]
        mines_index_list.append(mine_index)
        count += 1
    return mines_index_list

mines_places = random_mines_place()
def put_mines_on_screen(mines_places):
    for index in range(len(mines_places)):
        x_place = mines_places[index][0]
        y_place = mines_places[index][1]
        black_board.blit(consts.MINE_IMG, (x_place, y_place))



def night_soldier(x, y):
    black_board.blit(consts.SOLDIER_NIGHT_IMG, (x, y))


#
# pygame.display.flip()  # can put at the end of the main
# pygame.time.wait(10000)
