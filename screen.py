import pygame
import consts
import random
import game_field


mines_index_list = []

pygame.init() #should be in main

green_board = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("Game Of Life")
green_board.fill(consts.GREEN_COLOR)



def random_bushes_place(green_board):
    count = 0
    while count < 20:
        grass_x = random.randint(0, (consts.BOARD_COLUMNS * consts.SQUARE_SIZE - consts.SQUARE_SIZE * 2))
        grass_y = random.randint(0, (consts.BOARD_ROWS * consts.SQUARE_SIZE - consts.SQUARE_SIZE * 2))
        green_board.blit(consts.GRASS_IMG, (grass_x, grass_y))
        count += 1
def random_bushes_place():
    count = 0
    while count < 20:
        grass_x = random.randint(0, (consts.BOARD_COLUMNS * consts.SQUARE_SIZE) - 30)
        grass_y = random.randint(0, (consts.BOARD_ROWS * consts.SQUARE_SIZE) - 30)
        green_board.blit(consts.GRASS_IMG, (grass_x, grass_y))
        count += 1

def put_soldier_on_screen():
    green_board.blit(consts.SOLDIER_IMG, (0,0))

def put_flag_on_screen():
    green_board.blit(consts.FLAG_IMG, (consts.WINDOW_WIDTH - 4 * consts.SQUARE_SIZE, consts.WINDOW_HEIGHT - 3 * consts.SQUARE_SIZE))


def black_board():
    black_board = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    black_board.fill(consts.BLACK_COLOR)
    for x in range(0, consts.WINDOW_WIDTH, consts.SQUARE_SIZE):
        for y in range(0, consts.WINDOW_HEIGHT, consts.SQUARE_SIZE):
            rect = pygame.Rect(x, y, consts.SQUARE_SIZE, consts.SQUARE_SIZE)
            pygame.draw.rect(black_board, consts.GRID_GREEN_COLOR, rect, 1)

    random_mines_place(mines_index_list, black_board)

def random_mines_place(mines_index_list, black_board):
    count = 0
    while count < 20:
        mine_x = random.randint(0, (consts.BOARD_COLUMNS * consts.SQUARE_SIZE - consts.SQUARE_SIZE * 3))
        mine_y = random.randint(0, (consts.BOARD_ROWS * consts.SQUARE_SIZE - consts.SQUARE_SIZE))
        mine_index = [mine_x, mine_y]
        mines_index_list.append(mine_index)
        black_board.blit(consts.MINE_IMG, (mine_x, mine_y))
        count += 1

def draw_text(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    green_board.blit(text_img, location)


def draw_start_message():
    draw_text(consts.START_MESSAGE_1, consts.START_FONT_SIZE,
                 consts.START_COLOR, consts.START_MESSAGE_1_LOCATION)
    draw_text(consts.START_MESSAGE_2, consts.START_FONT_SIZE,
              consts.START_COLOR, consts.START_MESSAGE_2_LOCATION)

draw_start_message()
put_soldier_on_screen()
random_bushes_place()
put_flag_on_screen()
pygame.display.flip()  # can put at the end of the main
pygame.time.wait(10000)