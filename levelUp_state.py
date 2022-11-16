import pygame.mouse
from pico2d import *
import game_framework
import play_state


BG_image = None
Item_image = None
select_Number = 0
Type = None


def enter():
    pass

def exit():
    # fill here
    pass

def handle_events():
    global select_Number, Type
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            print(event.x, event.y)
            game_framework.quit()

        if event.type == SDL_QUIT:
            game_framework.quit()
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






