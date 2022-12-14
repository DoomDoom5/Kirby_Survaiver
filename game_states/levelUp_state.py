from pico2d import *
import game_framework
from game_states import play_state
import random
import server

levelUp_bgm = None
Item_image = None
select_Number = None
Type = None
box_bg_image = None
anim_height = None



Abilitys = ["방어력을 1 얻습니다" ,"공격을 5 얻습니다", "속도를 0.05 얻습니다", "얼음 능력을 획득/강화 합니다", "불 능력을 획득/강화 합니다", "번개 능력을 획득/강화 합니다",
            "동료 1의 무기를 강화합니다", "동료 2의 무기를 강화합니다"]
def Menu_Ability(menu_number, AbilityNumber):
    server.ui_Manager.UI_font.draw(550 , anim_height + 550 - menu_number * 120, Abilitys[AbilityNumber], (255, 255, 255))
    pass

a = None
def enter():
    print(play_state.kirby.weapons)
    global box_bg_image,anim_height , a,levelUp_bgm
    anim_height = 600
    box_bg_image = load_image("assets/Ui/UI.png")
    levelUp_bgm = load_wav("assets/sounds/VS_LevelUp_v02-02.ogg")
    play_state.kirby.x_dir, play_state.kirby.y_dir = 0 , 0

    a = random.sample(range(0, len(Abilitys)), 3)  # 1부터 10까지의 범위중에 3개를 중복없이 뽑겠다.
    print(a)
    levelUp_bgm.set_volume(server.masterVolume)
    levelUp_bgm.play(1)
    pass

def exit():
    global box_bg_image,anim_height
    del box_bg_image,anim_height
    # fill here
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            if event.x > 1280//2-550//2 and event.x < 1280//2+550//2 :
                print(event.x ,", ", event.y)
                if event.y < 210 and event.y > 110:
                    play_state.Player.select_Ability(a[0])
                    game_framework.pop_state()
                elif event.y < 330 and event.y > 230 :
                    play_state.Player.select_Ability(a[1])
                    game_framework.pop_state()
                elif event.y < 450 and  event.y > 350:
                    play_state.Player.select_Ability(a[2])
                    game_framework.pop_state()
        if event.type == SDL_QUIT:
            game_framework.quit()
    pass

def draw():
    clear_canvas()
    play_state.draw_world()

    box_bg_image.clip_draw(175,512 - 131 - 48,48,48,1280//2, anim_height + 720//2,800,720)


    for i in range(0,3):
        # x = 550 , y = 570 - i * 120
        box_bg_image.clip_draw(175,512 - 131 - 48,48,48,1280//2 , anim_height +720//2 + 200 - 120* i,550,100)
        Menu_Ability(i, a[i])

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






