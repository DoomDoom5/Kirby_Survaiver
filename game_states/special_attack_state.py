from pico2d import *

import game_world
import game_framework
from game_states import play_state


black_alpha_image =None
skill_time = None
skill_background = None
super_at_bgm = None
image_move_x = None
def enter():
    global black_alpha_image, skill_time,super_at_bgm, image_move_x,skill_background
    image_move_x = -1280//2
    black_alpha_image = load_image("assets/Ui/UI.png")
    black_alpha_image.opacify(0.5)

    skill_time = 2
    skill_background = load_image("assets/img/Effect/superAttack_image_blue.jpg")
    super_at_bgm= load_wav("assets/sounds/VS_SuperOn.wav")
    super_at_bgm.play(1)
    pass


def exit():
    global black_alpha_image, skill_time,super_at_bgm
    del black_alpha_image, skill_time,super_at_bgm
    # fill here
    pass


def handle_events():
    play_state.handle_events()
    pass


def draw():
    clear_canvas()
    play_state.draw_world()
    black_alpha_image.clip_draw(284,512 - 159 - 6, 6, 6, 1280//2, 720//2,1280,720)
    if skill_time > 1 :
        play_state.kirby.spacial_draw(play_state.kirby,image_move_x,skill_background )
    update_canvas()
    pass


def update():
    global skill_time, image_move_x
    play_state.update()
    skill_time -= game_framework.frame_time
    if image_move_x < -1280//4:
        image_move_x += 30
    elif skill_time <= 1 :
        play_state.kirby.spacial_Attack(play_state.kirby)

    if skill_time <= 0:
        game_framework.pop_state()
    pass


def pause():
    pass


def resume():
    pass






