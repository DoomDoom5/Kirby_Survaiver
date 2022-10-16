from pico2d import *
import game_framework
import random
from Character import Player
from Character import Enemy
from Manager import Enemy_Manager


max_col = 40
max_row = 40

kirby = Player()
Enemys = [Enemy() for i in range(0,10)]
BG_tile_image = None
UI_image = None
enemy_image = None
Timer = 0


def enter():
    global BG_tile_image, tiles, kirby, Enemys, enemy_image, UI_image
    BG_tile_image = load_image("assets/img/tilesets/ForestTexturePacked.png")
    UI_image = load_image("assets/Ui/UI.png")
    kirby.image = load_image("assets/img/Kirby/Ice_Kirby_empty.png")
    enemy_image= load_image("assets/img/Enemy/Normal_Enemy.png")
    kirby.type = "ICE"

    for s_Enemy in Enemys :
        s_Enemy.name = "Waddle_dee"
        s_Enemy.x = random.randint(0, 1280)
        s_Enemy.y = random.randint(0, 720)
        s_Enemy.__init__()
        pass
def exit():
    global BG_tile_image
    del BG_tile_image
    pass

def update():
    kirby.Move()
    if kirby.invisivleTime > 0 :
        kirby.invisivleTime -= 0.03

    for s_Enemy in Enemys :
        s_Enemy.chase(kirby.x , kirby.y)
        s_Enemy.Move()
        kirby.check_Enemy_Coll(s_Enemy.x - s_Enemy.width//2,
                               s_Enemy.x + s_Enemy.width//2,
                               s_Enemy.y + s_Enemy.height//2,
                               s_Enemy.y - s_Enemy.height//2,
                               s_Enemy.power)


    pass

def draw():
    global Timer
    clear_canvas()
    for col in range(0, max_col):
        for row in range(0, max_row):
            BG_tile_image.clip_draw(205,206,102,102, 102 * col, 102 * row, 110,110)
        pass

    # 경험치 출력
    UI_image.clip_draw(374, 512-249 -23, 10,23, 1280//2,700, 1280,40)

    for s_Enemy in Enemys:
        s_Enemy.draw(enemy_image)
        pass
    kirby.draw()
    # 체력 출력
    UI_image.clip_draw(280, 512-158 -9, 9,9, kirby.x, kirby.y - 30, 60,8)
    UI_image.clip_draw(422, 512-158 -9, 9,9, kirby.x, kirby.y - 30, kirby.Hp/kirby.MaxHp * 60,8)

    # 아이템 출력
    UI_image.clip_draw(175,512-98 - 32, 96,32 , 100, 720 - 75, 200, 200//3)


    update_canvas()

    Timer += 0.03
    delay(0.03)
    # fill here
    pass

def handle_events():
    events = get_events()
    kirby.handle_events(events)
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()






