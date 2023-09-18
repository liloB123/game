import pygame
import consts
import game_field

state = {
    "is_window_open" : True,
    "is_player_moving" : False,
    "moving_direction" : None,
    "soldier_state" : consts.START_LOC_SOLDIER,
    "flag_state" : consts.START_LOC_FLAG,
    "soldier_pic_loc_x" : consts.SOLDIER_PIC_LOC_X,
    "soldier_pic_loc_y" : consts.SOLDIER_PIC_LOC_Y,
    "state" : consts.RUNNING_STATE
}

def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False


        elif event.type == pygame.K_UP:
            move_player_up()

        elif event.type == pygame.K_DOWN:
            move_player_down()

        elif event.type == pygame.K_LEFT:
            move_player_left()

        elif event.type == pygame.K_RIGHT:
            move_player_right()

        elif event.type == pygame.K_SPACE:
            screen


def move_player_up():
    for row in range(state["soldier_state"]):
        if row > 0:
            for col in range(state["soldier_state"][row]):
                state["soldier_state"][row][col] = state["soldier_state"][row - 1][col]
    state["soldier_pic_loc_y"] -= consts.SQUARE_SIZE

    return state["soldier_state"]

def move_player_down():
    can_move = []
    for row in range(state["soldier_state"]):
        if row > 24:
            can_move.append(1)
    if can_move == []:
        for row in range(len(state["soldier_state"])):
            for col in range(len(state["soldier_state"][row])):
                state["soldier_state"][row][col] = state["soldier_state"][row + 1][col]
    state["soldier_pic_loc_y"] += consts.SQUARE_SIZE

    return state["soldier_state"]

def move_player_left():
    for row in range(state["soldier_state"]):
        for col in range(len(state["soldier_state"][row])):
            if col > 0:
                state["soldier_state"][row][col] = state["soldier_state"][row + 1][col]
    state["soldier_pic_loc_x"] -= consts.SQUARE_SIZE

    return state["soldier_state"]


def move_player_right():
    can_move = []
    for row in range(state["soldier_state"]):
        for col in range(len(state["soldier_state"][row])):
            if col > 49:
                can_move.append(1)
    if can_move == []:
        for row in range(state["soldier_state"]):
            for col in range(len(state["soldier_state"][row])):
                state["soldier_state"][row][col] = state["soldier_state"][row + 1][col]
    state["soldier_pic_loc_x"] -= consts.SQUARE_SIZE

    return state["soldier_state"]


def is_win():
    if game_field.check_if_touching_flag(state):
        return True
    else:
        return False

def is_lose():
    if game_field.check_if_touching_bomb(state):
        return True
    else:
        return False




