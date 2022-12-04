from pico2d import *

import game_world
import game_framework
from game_states import play_state


black_alpha_image =None
skill_time = None
def enter():
    global black_alpha_image, skill_time
    black_alpha_image = load_image("assets/Ui/UI.png")
    black_alpha_image.opacify(0.5)
    skill_time = 2
    pass


def exit():
    global black_alpha_image, skill_time
    del black_alpha_image, skill_time
    # fill here
    pass


def handle_events():
    play_state.handle_events()
    pass


def draw():
    clear_canvas()
    play_state.draw_world()
    black_alpha_image.clip_draw(284,512 - 159 - 6, 6, 6, 1280//2, 720//2,1280,720)
    play_state.kirby.spacial_draw(play_state.kirby)
    update_canvas()
    pass


def update():
    global skill_time
    play_state.update()
    skill_time -= game_framework.frame_time
    play_state.kirby.spacial_Attack(play_state.kirby)

    if skill_time <= 0:
        game_framework.pop_state()
    pass


def pause():
    pass


def resume():
    pass






