from pico2d import *
import game_framework
import server
from game_states import CharaterSelect_state
from game_states import comfig_state

bg_image = None
bg_bgm = None
start_button = None
close_button = None

def enter():
    global bg_image, start_button, close_button, bg_bgm,config_button
    bg_image = load_image("assets/title/BackGround.png")
    start_button = load_image("assets/title/bg_Button.png")
    config_button = load_image("assets/title/bg_Button.png")
    close_button = load_image("assets/title/bg_Button.png")
    bg_bgm = load_music("assets/sounds/bgm_titleintro.wav")
    bg_bgm.set_volume(server.masterVolume)
    bg_bgm.play(1)
    # fill here
    pass

def exit():
    # fill here
    global bg_image, start_button, close_button ,bg_bgm,config_button
    del bg_image, start_button, close_button, bg_bgm,config_button
    pass

def handle_events():
    # fill here
    global config_button, start_button, close_button,config_button

    events = get_events()
    for event in events:
        if event.x > 1000 and event.x < 1000 + 228 and 720 - event.y > 80 + 144 * 2 and  720 - event.y < 80 + 144 * 3:
            if event.type == SDL_MOUSEMOTION:
                start_button = load_image("assets/title/bg_Check_Button.png")
                config_button = load_image("assets/title/bg_Button.png")
                close_button = load_image("assets/title/bg_Button.png")
            elif event.type == SDL_MOUSEBUTTONDOWN:
                bg_bgm.stop()
                game_framework.change_state(CharaterSelect_state)

        elif event.x > 1000 and event.x < 1000 + 228 and 720 - event.y > 80+ 144 * 1 and 720 - event.y < 80 + 144 * 2:
            if event.type == SDL_MOUSEMOTION:
                start_button = load_image("assets/title/bg_Button.png")
                config_button = load_image("assets/title/bg_Check_Button.png")
                close_button = load_image("assets/title/bg_Button.png")
            elif event.type == SDL_MOUSEBUTTONDOWN:
                game_framework.push_state(comfig_state)


        elif event.x > 1000 and event.x < 1000 +228 and 720 - event.y > 80 and  720 - event.y < 80 + 144 * 1:
            if event.type == SDL_MOUSEMOTION:
                start_button = load_image("assets/title/bg_Button.png")
                config_button = load_image("assets/title/bg_Button.png")
                close_button = load_image("assets/title/bg_Check_Button.png")

            elif event.type == SDL_MOUSEBUTTONDOWN:
                game_framework.quit()
                pass

        elif event.type == SDL_QUIT:
            game_framework.quit()
    pass

def draw():
    clear_canvas()
    draw_title()
    update_canvas()


def draw_title():
    bg_image.draw(1280 // 2, 720 // 2)
    start_button.clip_draw(0, 0, 228, 144, 1100, 144 * 3)
    config_button.clip_draw(228, 0, 228, 144, 1100, 144 * 2)
    close_button.clip_draw(228 * 2, 0, 228, 144, 1100, 144)


def update():
    pass

def pause():
    pass

def resume():
    pass






