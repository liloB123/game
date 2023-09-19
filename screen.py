import pygame
import consts
import random

import game_field

bushes_index = []

pygame.init() #should be in main

def green_board():
    green_board = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_LENGTH))
    pygame.display.set_caption("Game Of Life")
    green_board.fill(consts.GREEN_COLOR)





# def random_bushes_index():
#     count = 0
#
#     while count < 20:
#         row_index = random.randint(0, 24)
#         column_index = random.randint(0, 49)
#         place_bushes(row_index, column_index)
#
#         # game_field.create_board()[row_index][column_index] ==
#         # bush_index = [bush_row_index, bush_column_index]
#         # if bush_index not in bushes_index:
#         #     bushes_index.append(bush_index)
#         #     count += 1
#
#
# def place_bushes(row_index, column_index):
#     game_field.create_board()[row_index][column_index] = pygame.image.load(consts.GRASS_IMG)
#     # bush = pygame.image.load(consts.GRASS_IMG)
#     # for bush_index in bushes_index:
#     #     bush_row = bush_index[0]
#     #     bush_column = bush_index[1]
#     #     game_field.create_board()[bush_row][bush_column] = bush
#         # y_coordinate = bush_row * consts.SQUARE_SIZE
#         # x_coordinate = bush_column * consts.SQUARE_SIZE
#         # bush.blit(y_coordinate, x_coordinate)


green_board()
# random_bushes_index()

pygame.display.flip()  # can put at the end of the main
pygame.time.wait(10000)