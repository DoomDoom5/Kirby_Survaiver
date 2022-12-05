from pico2d import *
import game_framework
from game_states import mapSelect_state
class Kirby_UI:
    kirby_type = None
    c_kirby_UI_image = None
    x = None
    y = None
    width = None
    Height = None

# fill here
bg_image = None
bg_bgm = None
box_bg_image = None
UI_button_image = None

start_Button = None
select_Button = None
cancel_Button = None

Type = "Test"
kirbys = None
select_Number = None

def enter():
    global bg_image, box_bg_image, UI_button_image,select_Number, kirbys, bg_bgm
    kirbys = Kirby_UI()
    kirbys.c_kirby_UI_image = load_image("assets/Ui/Kirby_UI.png")
    select_Number = -1
    bg_image = load_image("assets/Ui/introBG.png")
    bg_bgm = load_music("assets/sounds/bgm_select.wav")

    box_bg_image = load_image("assets/Ui/UI.png")
    UI_button_image = load_image("assets/Ui/UI.png")

    bg_bgm.repeat_play()

    # fill here
    pass

def exit():
    global bg_image,UI_button_image, box_bg_image,kirbys,select_Number,bg_bgm
    del bg_image, UI_button_image,box_bg_image,kirbys,select_Number,bg_bgm
    # fill here
    pass

def update():

    # fill here
    pass

def draw():
    clear_canvas()

    bg_image.clip_draw(0,0,400,300,1280//2,720//2,1280,720)
    box_bg_image.clip_draw(175,512 - 131 - 48,48,48,1280//2,720//2,800,720)
    for i in range(0,3):
        if select_Number == -1 or select_Number != i:
            box_bg_image.clip_draw(175,512 - 131 - 48, 48, 48, 1280//2 - 250 + i * 125, 720 - 200,100,100)
        else :
            box_bg_image.clip_draw(419, 512 - 98 - 48, 48, 48, 1280 // 2 - 250 + i * 125, 720 - 200, 100, 100)
            UI_button_image.clip_draw(176, 512 - 181 - 33, 48, 33, 850, 150, 100, 60)
            pass
        kirbys.c_kirby_UI_image.clip_draw(0,160 - 32 * i, 32, 32, 1280//2 - 250 + i * 125, 720 - 200,70,70)


    update_canvas()
    # fill here
    pass

def handle_events():
    global select_Number, Type, subType_1 ,subType_2
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            print(event.x, event.y)
            if event.x > 800 and event.x < 900 and event.y > 540 and event.y < 600 and select_Number != -1: # 캐릭터 선택하고 다음 시작
                match select_Number:
                    case 0:
                        Type = "FIRE"
                        subType_1 = "ICE"
                        subType_2 = "PLASMA"
                    case 1:
                        Type = "ICE"
                        subType_1 = "FIRE"
                        subType_2 = "PLASMA"
                    case 2:
                        Type = "PLASMA"
                        subType_1 = "ICE"
                        subType_2 = "FIRE"
                game_framework.change_state(mapSelect_state)

                pass
            else:
                for select in range(0,5):
                    if event.x > 1280//2 - 250 + select * 125 - 35 and event.x < 1280//2 - 250 + select * 125 + 35 and event.y > 150 and event.y < 250 :
                        select_Number = select

                    pass
        if event.type == SDL_QUIT:
            game_framework.quit()





