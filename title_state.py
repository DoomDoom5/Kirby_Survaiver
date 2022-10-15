import pygame.mouse
from pico2d import *
import game_framework
import play_state
import logo_state

bg_image = None
start_button = None
config_button = None
close_button = None



def enter():
    global bg_image, start_button, close_button,config_button
    bg_image = load_image("assets/title/BackGround.png")
    start_button = load_image("assets/title/bg_Button.png")
    config_button = load_image("assets/title/bg_Button.png")
    close_button = load_image("assets/title/bg_Button.png")
    # fill here
    pass

def exit():
    # fill here
    global bg_image, start_button, close_button
    del bg_image, start_button, close_button
    pass

def handle_events():
    # fill here
    global config_button, start_button, close_button

    events = get_events()
    for event in events:
        if event.x > 1000 and event.x < 1000 + 228 and 720 - event.y > 80 + 144 * 2 and  720 - event.y < 80 + 144 * 3:
            if event.type == SDL_MOUSEMOTION:
                start_button = load_image("assets/title/bg_Check_Button.png")
                config_button = load_image("assets/title/bg_Button.png")
                close_button = load_image("assets/title/bg_Button.png")
            elif event.type == SDL_MOUSEBUTTONDOWN:
                game_framework.change_state(logo_state)

        elif event.x > 1000 and event.x < 1000 + 228 and 720 - event.y > 80 + 144 * 1  and  720 - event.y < 80 + 144 * 2:
            if event.type == SDL_MOUSEMOTION:
                start_button = load_image("assets/title/bg_Button.png")
                config_button = load_image("assets/title/bg_Check_Button.png")
                close_button = load_image("assets/title/bg_Button.png")

            elif event.type == SDL_MOUSEBUTTONDOWN:
                pass


        elif event.x > 1000 and event.x < 1000 +228 and 720 - event.y > 80 and  720 - event.y < 80 + 144 * 1:
            if event.type == SDL_MOUSEMOTION:
                start_button = load_image("assets/title/bg_Button.png")
                config_button = load_image("assets/title/bg_Button.png")
                close_button = load_image("assets/title/bg_Check_Button.png")

            elif event.type == SDL_MOUSEBUTTONDOWN:
                game_framework.quit()
                pass



        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(logo_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                pass
    delay(0.01)
    pass

def draw():
    clear_canvas()
    bg_image.draw(1280//2, 720//2)

    start_button.clip_draw(0, 0,    228, 144,    1100, 144*3)
    config_button.clip_draw(228, 0, 228, 144,   1100, 144*2)
    close_button.clip_draw(228*2, 0, 228, 144,   1100, 144)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass






