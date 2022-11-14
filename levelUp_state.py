import pygame.mouse
from pico2d import *
import game_framework
import play_state


BG_image = None
Item_image = None



def enter():
    pass

def exit():
    # fill here
    pass

def handle_events():
    events = get_events()
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    update_canvas()
    pass

def update():
    play_state.update()
    pass

def pause():
    pass

def resume():
    pass






