import pygame
import consts
import random

mines_index_list = []


black_board = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
black_board.fill(consts.BLACK_COLOR)
for x in range(0, consts.WINDOW_WIDTH, consts.SQUARE_SIZE):
    for y in range(0, consts.WINDOW_HEIGHT, consts.SQUARE_SIZE):
        rect = pygame.Rect(x, y, consts.SQUARE_SIZE, consts.SQUARE_SIZE)
        pygame.draw.rect(black_board, consts.GRID_GREEN_COLOR, rect, 1)

def random_mines_place(mines_index_list, black_board):
    count = 0
    while count < 20:
        mine_x = random.randint(0, (consts.BOARD_COLUMNS * consts.SQUARE_SIZE - consts.SQUARE_SIZE * 3))
        mine_y = random.randint(0, (consts.BOARD_ROWS * consts.SQUARE_SIZE - consts.SQUARE_SIZE))
        mine_index = [mine_x, mine_y]
        mines_index_list.append(mine_index)
        black_board.blit(consts.MINE_IMG, (mine_x, mine_y))
        count += 1


def night_soldier(black_board):
    black_board.blit(consts.SOLDIER_NIGHT_IMG, (0, 0))

random_mines_place(mines_index_list, black_board)
night_soldier(black_board)
pygame.display.flip()  # can put at the end of the main
pygame.time.wait(10000)
