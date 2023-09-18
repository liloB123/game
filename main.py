import pygame
import consts

state = {
    "is_window_open" : True,
    "is_player_moving" : False,
    "moving_direction" : None,
    "soldier_state" : consts.START_LOC_SOLDIER,
    "flag_state" : consts.START_LOC_FLAG
}

def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False


        elif event.type == pygame.K_UP:
            move_player_up() #needs to be def

        elif event.type == pygame.K_DOWN:
            move_player_down() #needs to be def

        elif event.type == pygame.K_LEFT:
            move_player_left() #needs to be def

        elif event.type == pygame.K_RIGHT:
            move_player_right() #needs to be def


def move_player_up():
    for pixel in range(len(state["soldier_state"])):
        state["soldier_state"][pixel] = state["soldier_state"][pixel + 1]

    state["soldier_state"]