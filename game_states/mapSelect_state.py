from pico2d import *
import game_framework
from game_states import play_state

# fill here
bg_image = None
box_bg_image = None
UI_button_image = None

start_Button = None
select_Button = None

font = None
Type = None
select_Number = None

def enter():
    global bg_image, box_bg_image, UI_button_image,font, Type,select_Number
    bg_image = load_image("assets/Ui/introBG.png")
    box_bg_image = load_image("assets/Ui/UI.png")
    UI_button_image = load_image("assets/Ui/UI.png")
    font  = load_font("assets/Ui/NEXONFootballGothicL.ttf", 20)
    Type = "Test"
    select_Number = -1

    # fill here
    pass

def exit():
    global bg_image,UI_button_image, box_bg_image, font
    del bg_image, UI_button_image,box_bg_image, font
    # fill here
    pass

def update():

    # fill here
    pass

def draw():
    clear_canvas()
    global Type
    bg_image.clip_draw(0,0,400,300,1280//2,720//2,1280,720)
    box_bg_image.clip_draw(175,512 - 131 - 48,48,48,1280//2,720//2,800,720)

    UI_button_image.clip_draw(0 , 512 - 97 , 158 , 97  , 1280//2 - 150, 720//2 + 150, 300,200)
    UI_button_image.clip_draw(314 , 512 - 97 , 158 , 97  , 1280//2 - 150 , 720//2 -100, 300,200)
    font.draw(1280//2 + 100, 720 - 120, "맵을 선택해 주세요", (255, 255, 255))

    if select_Number != -1:
        match select_Number:
            case 0:
                Type  = 0
                UI_button_image.clip_draw(0, 512 - 97, 158, 97, 1280 // 2 + 200, 720 // 2, 350, 230)
            case 1:
                Type  = 1
                UI_button_image.clip_draw(314, 512 - 97, 158, 97, 1280 // 2 + 200, 720 // 2, 350, 230)

        UI_button_image.clip_draw(176, 512 - 181 - 33, 48, 33, 850, 150, 100, 60)
        font.draw(830, 720 - 570, "시작", (255, 255, 255))
        pass

    update_canvas()
    # fill here
    pass

def handle_events():
    global select_Number, Type
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            print(event.x, event.y)
            if event.x > 340 and event.x < 640 and event.y > 100 and event.y < 300 : # 맵 선택
                select_Number = 0

            elif  event.x > 340 and event.x < 640 and event.y > 350 and event.y < 550 :
                select_Number = 1

            elif select_Number != -1 and event.x > 800 and event.x < 900 and event.y > 540 and event.y < 600 :
                game_framework.change_state(play_state)


        if event.type == SDL_QUIT:
            game_framework.quit()



