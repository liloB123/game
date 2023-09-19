import pygame
import consts
import random


pygame.init() #should be in main


green_board = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))



def print_green_screen(state):
    pygame.display.set_caption("Game Of Life")
    green_board.fill(consts.GREEN_COLOR)
    put_bushes_on_screen(bushes_places)
    put_soldier_on_screen(state["soldier_pic_loc_x"],state["soldier_pic_loc_y"])
    put_flag_on_screen()
    if state["soldier_pic_loc_x"] == 0 and state["soldier_pic_loc_y"] == 0:
        draw_start_message()
    if state["state"] == consts.WIN_STATE:
        draw_win()

    if state["state"] == consts.LOSE_STATE:
        draw_lose()


    pygame.display.flip()

def random_bushes_place():
    bushes_places = []
    count = 0
    while count < 20:
        grass_x = random.randint(0, (consts.BOARD_COLUMNS * consts.SQUARE_SIZE - consts.SQUARE_SIZE * 2))
        grass_y = random.randint(0, (consts.BOARD_ROWS * consts.SQUARE_SIZE - consts.SQUARE_SIZE * 2))
        bush = [grass_x, grass_y]
        bushes_places.append(bush)
        count += 1
    return bushes_places

bushes_places = random_bushes_place()

def put_bushes_on_screen(bushes_places):
    for index in range(len(bushes_places)):
        x_place = bushes_places[index][0]
        y_place = bushes_places[index][1]
        green_board.blit(consts.GRASS_IMG, (x_place, y_place))


def put_soldier_on_screen(x,y):
    green_board.blit(consts.SOLDIER_IMG, (x,y))

def put_flag_on_screen():
    green_board.blit(consts.FLAG_IMG, (consts.WINDOW_WIDTH - 4 * consts.SQUARE_SIZE, consts.WINDOW_HEIGHT - 3 * consts.SQUARE_SIZE))

def draw_text(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    green_board.blit(text_img, location)
    # pygame.time.delay(3000)


def draw_start_message():
    draw_text(consts.START_MESSAGE_1, consts.START_FONT_SIZE,
                 consts.START_COLOR, consts.START_MESSAGE_1_LOCATION)
    draw_text(consts.START_MESSAGE_2, consts.START_FONT_SIZE,
              consts.START_COLOR, consts.START_MESSAGE_2_LOCATION)

def draw_lose():
    draw_text(consts.LOSE_MESSAGE, consts.END_FONT_SIZE,
              consts.END_COLOR, consts.END_MESSAGE_LOCATION)


def draw_win():
    draw_text(consts.WIN_MESSAGE, consts.END_FONT_SIZE,
              consts.END_COLOR, consts.END_MESSAGE_LOCATION)





#
# pygame.display.flip()  # can put at the end of the main
# pygame.time.wait(10000)
