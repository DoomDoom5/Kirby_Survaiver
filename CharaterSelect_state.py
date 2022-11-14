from pico2d import *
import game_framework
import play_state
class Kirby_UI:
    kirby_type = None
    c_kirby_UI_image = None
    x = None
    y = None
    width = None
    Height = None

# fill here
bg_image = None
box_bg_image = None
UI_button_image = None

start_Button = None
select_Button = None
cancel_Button = None

Type = "Test"
kirbys = Kirby_UI()
select_Number = -1

def enter():
    global bg_image, box_bg_image, UI_button_image
    global kirbys
    bg_image = load_image("assets/Ui/introBG.png")
    box_bg_image = load_image("assets/Ui/UI.png")
    UI_button_image = load_image("assets/Ui/UI.png")
    kirbys.c_kirby_UI_image = load_image("assets/Ui/Kirby_UI.png")

    # fill here
    pass

def exit():
    global bg_image,UI_button_image, box_bg_image
    del bg_image, UI_button_image,box_bg_image
    # fill here
    pass

def update():

    # fill here
    pass

def draw():
    clear_canvas()

    bg_image.clip_draw(0,0,400,300,1280//2,720//2,1280,720)
    box_bg_image.clip_draw(175,512 - 131 - 48,48,48,1280//2,720//2,800,720)
    for i in range(0,5):
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
    global select_Number, Type
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            print(event.x, event.y)
            if event.x > 800 and event.x < 900 and event.y > 540 and event.y < 600 and select_Number != -1: # 캐릭터 선택하고 다음 시작
                match select_Number:
                    case 0:
                        Type = "FIRE"
                    case 1:
                        Type = "ICE"
                    case 2:
                        Type = "PLASMA"
                    case 3:
                        Type = "HAMMER"
                    case 4:
                        Type = "SWORD"
                game_framework.change_state(play_state)

                pass
            else:
                for select in range(0,5):
                    if event.x > 1280//2 - 250 + select * 125 - 35 and event.x < 1280//2 - 250 + select * 125 + 35 and event.y > 150 and event.y < 250 :
                        select_Number = select

                    pass
        if event.type == SDL_QUIT:
            game_framework.quit()





