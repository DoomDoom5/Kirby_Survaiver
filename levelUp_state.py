import pygame.mouse
from pico2d import *
import game_framework
import play_state
import random

Item_image = None
select_Number = 0
Type = None
box_bg_image = None
anim_height = None


a = random.sample(range(0,100),10) # 1부터 100까지의 범위중에 10개를 중복없이 뽑겠다.
def enter():
    global box_bg_image,anim_height
    anim_height = 600
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
            print(select_Number)
            if event.x > 1280//2-550//2 and event.x < 1280//2+550//2 :
                if event.y < 200 and event.y > 100:
                    play_state.kirby.select_Ability(0)
                    game_framework.pop_state()
                elif event.y < 330 and event.y > 230 :
                    play_state.kirby.select_Ability(1)
                    game_framework.pop_state()
                elif event.y < 450 and  event.y > 350:
                    play_state.kirby.select_Ability(2)
                    game_framework.pop_state()



        if event.type == SDL_QUIT:
            game_framework.quit()
    pass

def draw():
    clear_canvas()
    play_state.draw_world()

    box_bg_image.clip_draw(175,512 - 131 - 48,48,48,1280//2, anim_height + 720//2,800,720)


    for i in range(0,3):
        box_bg_image.clip_draw(175,512 - 131 - 48,48,48,1280//2 , anim_height +720//2 + 200 - 120* i,550,100)
        play_state.ui_Manager.UI_font.draw(550,  anim_height +570, '최대체력을 %d 얻습니다' %10, (255, 255, 255))

        box_bg_image.clip_draw(175,512 - 131 - 48,48,48,1280//2 , anim_height +720//2 + 80,550,100)
        play_state.ui_Manager.UI_font.draw(550,  anim_height +450, '공격력을 %d 얻습니다' %5, (255, 255, 255))

        box_bg_image.clip_draw(175,512 - 131 - 48,48,48,1280//2, anim_height +720//2  - 40 ,550,100)
        play_state.ui_Manager.UI_font.draw(550,  anim_height +330, '스피드를 %3.1f 얻습니다' %0.1, (255, 255, 255))


    update_canvas()
    pass

def update():
    global anim_height
    if anim_height > 1:
        anim_height -= 100
    delay(0.02)
    pass

def pause():
    pass

def resume():
    pass






