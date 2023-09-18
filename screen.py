import pygame
import consts
import random

pygame.init() #should be in main

def green_board():
    green_board = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_LENGTH))
    pygame.display.set_caption("Game Of Life")

    green_board.fill(consts.GREEN_COLOR)


def random_bushes_index():
    bushes_index = []
    count = 0

    while count < 20:
        bush_row_index = random.randint(0, 24)
        bush_column_index = random.randint(0, 49)
        bush = [bush_row_index, bush_column_index]
        if bush not in bushes_index:
            bushes_index.append(bush)
            count += 1






# pygame.display.flip()  # can put at the end of the main
# pygame.time.wait(10000)