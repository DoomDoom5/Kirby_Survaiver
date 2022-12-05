from pico2d import *
import server
import game_framework
from game_states import title_state

box_bg_image = None
font = None

def enter():
    global box_bg_image , font
    box_bg_image = load_image("assets/Ui/UI.png")
    font  = load_font("assets/Ui/NEXONFootballGothicL.ttf", 20)
    # fill here
    pass

def exit():
    # fill here
    pass

def handle_events():
    # fill here

    events = get_events()
    for event in events:
        if event.x > 410 and event.x < 520 and event.y >240 and event.y < 290:
            if event.type == SDL_MOUSEBUTTONDOWN:
                if server.masterVolume < 100:
                    server.masterVolume += 1
        elif event.x > 410 and event.x < 520 and event.y >340 and event.y < 390:
            if event.type == SDL_MOUSEBUTTONDOWN:
                if server.masterVolume > 0:
                    server.masterVolume -= 1

        elif event.x > 800 and event.x < 900 and event.y > 560 and event.y < 600:
            if event.type == SDL_MOUSEBUTTONDOWN:
                game_framework.pop_state()
            pass
    pass

def draw():
    clear_canvas()
    title_state.draw_title()
    box_bg_image.clip_draw(175, 512 - 131 - 48, 48, 48, 1280 // 2,  720 // 2, 800, 720)
    font.draw(430, 720 - 170, "Master Volume : %d" % server.masterVolume, (255, 255, 255))

    box_bg_image.clip_draw(176, 512 - 181 - 33, 48, 33, 470, 720 - 270, 130, 60)
    font.draw(430, 720 - 270, "볼륨 증가", (255, 255, 255))

    box_bg_image.clip_draw(176, 512 - 181 - 33, 48, 33, 470, 720 - 370, 130, 60)
    font.draw(430, 720 - 370, "볼륨 하락", (255, 255, 255))
    
    

    font.draw(630, 720 - 440, "화살표로 캐릭터를 조종합니다.", (255, 255, 255))
    font.draw(630, 720 - 470, "게임 좌측에 게이지에서 READY가 뜰때", (255, 255, 255))
    font.draw(630, 720 - 500, "TAB을 누르면 필살기가 발동됩니다", (255, 255, 255))

    box_bg_image.clip_draw(176, 512 - 181 - 33, 48, 33, 850, 150, 100, 60)
    font.draw(830, 720 - 570, "뒤로", (255, 255, 255))
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass






