import pygame

import black_screen
import consts
import game_field
import screen
import soldier

state = {
    "is_window_open" : True,
    "is_player_moving" : False,
    "moving_direction" : None,
    "soldier_state" : soldier.soldier_start_loc(),
    "flag_state" : consts.START_LOC_FLAG,
    "soldier_pic_loc_x" : consts.SOLDIER_PIC_LOC_X,
    "soldier_pic_loc_y" : consts.SOLDIER_PIC_LOC_Y,
    "state" : consts.RUNNING_STATE
}



def main():
    pygame.init()
    black_screen.random_mines_place()

    while state["is_window_open"]:
        handle_user_events()
        game_field.mines_on_board(state)
        screen.print_green_screen(state)

def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_player_up()

            elif event.key == pygame.K_DOWN:
                move_player_down()

            elif event.key == pygame.K_LEFT:
                move_player_left()

            elif event.key == pygame.K_RIGHT:
                move_player_right()

            elif event.key == pygame.K_SPACE:
                black_screen.print_black_screen(state)
                pygame.time.delay(1000)



def move_player_up():
    can_move = []
    for index in state["soldier_state"]:
        if index[0] > 0:
            can_move.append(1)
        if len(can_move) == 8:
            for i in state["soldier_state"]:
                i[0] = i[0] - 1
            state["soldier_pic_loc_y"] -= consts.SQUARE_SIZE

    # return state["soldier_state"]

def move_player_down():
    can_move = []
    for index in state["soldier_state"]:
        if index[0] < 24:
            can_move.append(1)
    if len(can_move) == 8:
        for i in state["soldier_state"]:
            i[0] = i[0] + 1
        state["soldier_pic_loc_y"] += consts.SQUARE_SIZE
    # return state["soldier_state"]



def move_player_left():
    can_move = []
    for index in state["soldier_state"]:
        if index[1] > 0:
            can_move.append(1)
    if len(can_move) == 8:
        for i in state["soldier_state"]:
            i[1] = i[1] - 1
        state["soldier_pic_loc_x"] -= consts.SQUARE_SIZE

    # return state["soldier_state"]



def move_player_right():
    can_move = []
    for index in state["soldier_state"]:
        if index[1] < 49:
            can_move.append(1)
    if len(can_move) == 8:
        for i in state["soldier_state"]:
            i[1] = i[1] + 1
        state["soldier_pic_loc_x"] += consts.SQUARE_SIZE

    # return state["soldier_state"]

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


game_field.mines_on_board(state)

# if __name__ == '__main__':
#     main()
