import pygame.mouse
from pico2d import *
import game_framework
import play_state


Item_image = None
select_Number = 0
Type = None
box_bg_image = None

def enter():
    global box_bg_image

    play_state.kirby.x_dir = 0
    play_state.kirby.y_dir = 0
    box_bg_image = load_image("assets/Ui/UI.png")
    pass

def exit():
    global box_bg_image
    del box_bg_image
    # fill here
    pass

def handle_events():
    global select_Number, Type
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            print("클릭")
            game_framework.pop_state()

        if event.type == SDL_QUIT:
            game_framework.quit()
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    box_bg_image.clip_draw(175,512 - 131 - 48,48,48,1280//2,720//2,800,720)
    play_state.ui_Manager.UI_font.draw(300, 600, '최대체력을 %d 얻습니다)' %10, (255, 255, 255))
    play_state.ui_Manager.UI_font.draw(300, 500, '공격력을 %d 얻습니다)' %10, (255, 255, 255))
    play_state.ui_Manager.UI_font.draw(300, 400, '스피드를 %3.2f 얻습니다)' %0.1, (255, 255, 255))


    update_canvas()
    pass

def update():
    pass

def pause():
    pass

def resume():
    pass






