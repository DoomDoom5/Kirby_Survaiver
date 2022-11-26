import pygame.mouse
from pico2d import *
import game_framework
import play_state



def enter():
    play_state.kirby.x_dir, play_state.kirby.y_dir = 0, 0

    pass


def exit():
    global box_bg_image
    del box_bg_image
    # fill here
    pass


def handle_events():
    pass


def draw():
    clear_canvas()
    play_state.draw_world()
    update_canvas()
    pass


def update():
    pass


def pause():
    pass


def resume():
    pass






