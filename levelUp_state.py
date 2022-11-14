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
            if event.x > 800 and event.x < 900 and event.y > 540 and event.y < 600 and select_Number != -1:  # 캐릭터 선택하고 다음 시작
                match select_Number:
                    case 0:
                        play_state.Weapons.append()
                    case 1:
                        play_state.Weapons
                    case 2:
                        play_state.Weapons
                game_framework.change_state(play_state)

                pass
            else:
                for select in range(0, 5):
                    if event.x > 1280 // 2 - 250 + select * 125 - 35 and event.x < 1280 // 2 - 250 + select * 125 + 35 and event.y > 150 and event.y < 250:
                        select_Number = select

                    pass
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






