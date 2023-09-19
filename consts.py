import pygame

START_LOC_SOLDIER = 1 #temp
START_LOC_FLAG = 2 #temp
SOLDIER_PIC_LOC_X = 0
SOLDIER_PIC_LOC_Y = 0

BOARD_ROWS = 25
BOARD_COLUMNS = 50
SQUARE_SIZE = 15
WINDOW_WIDTH = BOARD_COLUMNS * SQUARE_SIZE
WINDOW_HEIGHT = BOARD_ROWS * SQUARE_SIZE
GREEN_COLOR = (6, 140, 48)
BLACK_COLOR = (0, 0 ,0)
GRID_GREEN_COLOR = (64, 117, 50)

grass_image = pygame.image.load("grass.png")
DEFAULT_GRASS_SIZE = (SQUARE_SIZE * 2, SQUARE_SIZE * 2)
GRASS_IMG = pygame.transform.scale(grass_image, DEFAULT_GRASS_SIZE)

mine_ing = pygame.image.load("mine.png")
DEFAULT_MINE_SIZE = (SQUARE_SIZE * 3, SQUARE_SIZE)
MINE_IMG = pygame.transform.scale(mine_ing, DEFAULT_MINE_SIZE)

LOSE_STATE = 1
WIN_STATE = 3
RUNNING_STATE = 2



soldier_image = pygame.image.load("soldier.png")
DEFAULT_SOLDIER_SIZE = (SQUARE_SIZE * 2, SQUARE_SIZE * 4)
SOLDIER_IMG = pygame.transform.scale(soldier_image, DEFAULT_SOLDIER_SIZE)

flag_image = pygame.image.load("flag.png")
DEFAULT_FLAG_SIZE = (SQUARE_SIZE * 4, SQUARE_SIZE * 3)
FLAG_IMG = pygame.transform.scale(flag_image, DEFAULT_FLAG_SIZE)

FONT_NAME = "Calibri"
START_MESSAGE_1 = "Welcome to The Flag game."
START_MESSAGE_2 = "Have Fun!"
START_FONT_SIZE = int(0.02 * WINDOW_WIDTH)
START_COLOR = (255, 255, 255)
START_MESSAGE_1_LOCATION = \
    (0.05 * WINDOW_WIDTH, WINDOW_HEIGHT / 18 - (START_FONT_SIZE / 2))
START_MESSAGE_2_LOCATION = \
    (0.05 * WINDOW_WIDTH, WINDOW_HEIGHT/ 10 - (START_FONT_SIZE / 2))
