import pygame
import consts
import random


pygame.init() #should be in main


green_board = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("Game Of Life")
green_board.fill(consts.GREEN_COLOR)



def random_bushes_place():
    count = 0
    while count < 20:
        grass_x = random.randint(0, (consts.BOARD_COLUMNS * consts.SQUARE_SIZE - consts.SQUARE_SIZE * 2))
        grass_y = random.randint(0, (consts.BOARD_ROWS * consts.SQUARE_SIZE - consts.SQUARE_SIZE * 2))
        green_board.blit(consts.GRASS_IMG, (grass_x, grass_y))
        count += 1


def put_soldier_on_screen():
    green_board.blit(consts.SOLDIER_IMG, (0, 0))


def put_flag_on_screen():
    green_board.blit(consts.FLAG_IMG, (consts.WINDOW_WIDTH - 4 * consts.SQUARE_SIZE, consts.WINDOW_HEIGHT - 3 * consts.SQUARE_SIZE))


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
