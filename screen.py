import pygame
import consts

pygame.init() #should be in main

def green_board():
    green_board = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_LENGTH))
    pygame.display.set_caption("Game Of Life")

    green_board.fill(consts.GREEN_COLOR)
    pygame.display.flip()

def random_bushes():



# pygame.time.wait(10000)