import pygame
import consts
import random
import game_field

bushes_index = []

pygame.init() #should be in main

green_board = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_LENGTH))
pygame.display.set_caption("Game Of Life")
green_board.fill(consts.GREEN_COLOR)


def random_bushes_place():
    count = 0
    while count < 20:
        grass_x = random.randint(0, consts.BOARD_COLUMNS * consts.SQUARE_SIZE)
        grass_y = random.randint(0, consts.BOARD_ROWS * consts.SQUARE_SIZE)
        green_board.blit(consts.GRASS_IMG, (grass_x, grass_y))
        count += 1


random_bushes_place()
pygame.display.flip()  # can put at the end of the main
pygame.time.wait(10000)