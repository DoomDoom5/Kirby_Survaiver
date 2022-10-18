from pico2d import *
import game_framework
import random
import CharaterSelect_state
from Character import Player
from Character import Enemy
from Manager.Item_Manager import Missile_manager
from Manager.Item_Manager import Weapon
from Manager.Item_Manager import Item_manager
from Manager.Ui_Manager import Item_UI_Manager


missile_manager = Missile_manager()
item_manager = Item_manager()
item_UI_Manager = Item_UI_Manager()
Weapons = []

max_col = 40
max_row = 40

kirby = Player()
Enemys = [Enemy() for i in range(0,10)]
BG_tile_image = None
UI_image = None
enemy_image = None
Timer = 0
fps = 0.01
enemy_responTimer = 0


def enter():
    global BG_tile_image, tiles, kirby, Enemys, enemy_image, UI_image, Weapons,item_manager
    BG_tile_image = load_image("assets/img/tilesets/ForestTexturePacked.png")
    UI_image = load_image("assets/Ui/UI.png")
    enemy_image= load_image("assets/img/Enemy/Normal_Enemy.png")
    missile_manager.missiles_image = load_image("assets/img/Effect/vfx.png")
    item_manager.Items_image = load_image("assets/Ui/items.png")

    Kirby_init_Test(Weapons, kirby)

    for s_Enemy in Enemys :
        s_Enemy.name = "Waddle_dee"
        s_Enemy.__init__()
        pass




def exit():
    global BG_tile_image
    del BG_tile_image
    pass

def update():
    global enemy_responTimer, Timer
    if kirby.invisivleTime > 0 :
        kirby.invisivleTime -= fps
    missile_manager.Move()

    Kriby_Update()

    for s_Enemy in Enemys :
        s_Enemy.chase(kirby.x , kirby.y)
        s_Enemy.Move()
        s_Enemy.On_damege( missile_manager.Check_Hit_Enemy(s_Enemy.x - s_Enemy.width // 2,
                                        s_Enemy.x + s_Enemy.width // 2,
                                        s_Enemy.y + s_Enemy.height // 2,
                                        s_Enemy.y - s_Enemy.height // 2))
        if s_Enemy.Hp <= 0 :
            item_manager.Create_EXP_Stone(s_Enemy.name, s_Enemy.x, s_Enemy.y)
            Enemys.remove(s_Enemy)
        kirby.check_Enemy_Coll(s_Enemy.x - s_Enemy.width//2,
                               s_Enemy.x + s_Enemy.width//2,
                               s_Enemy.y + s_Enemy.height//2,
                               s_Enemy.y - s_Enemy.height//2,
                               s_Enemy.power)
    for weapon in Weapons:
        weapon.shot(kirby.x, kirby.y, kirby.invers, missile_manager)


    if enemy_responTimer >= 3.0:
        if Timer > 30.0:
            newEnemy = Enemy()
            newEnemy.name = "kinght"
            newEnemy.__init__()
            Enemys.append(newEnemy)
            enemy_responTimer = 0
        else:
            newEnemy = Enemy()
            newEnemy.name = "Waddle_dee"
            newEnemy.__init__()
            Enemys.append(newEnemy)
            enemy_responTimer = 0
    else:
        enemy_responTimer += fps
    pass


def Kriby_Update():
    kirby.Move()
    kirby.levelUP()
    kirby.Exp += item_manager.GainExp(kirby.x, kirby.y, kirby.Magent, kirby.Exp)


def draw():
    global Timer
    clear_canvas()
    for col in range(0, max_col):
        for row in range(0, max_row):
            BG_tile_image.clip_draw(205,206,102,102, 102 * col, 102 * row, 110,110)
        pass

    for s_Enemy in Enemys:
        s_Enemy.draw(enemy_image)
        UI_image.clip_draw(280, 512-158 -9, 9,9, s_Enemy.x, s_Enemy.y + 10, 30,4)
        UI_image.clip_draw(422, 512-158 -9, 9,9, s_Enemy.x, s_Enemy.y + 10, s_Enemy.Hp/s_Enemy.MaxHp * 30,4)
        pass

    missile_manager.draw()
    item_manager.Draw()

    kirby.draw()
    draw_UI()
    update_canvas()

    Timer += fps
    delay(fps)
    # fill here
    pass


def draw_UI():
    # 체력 출력
    UI_image.clip_draw(280, 512 - 158 - 9, 9, 9, kirby.x, kirby.y - 30, 60, 8)
    UI_image.clip_draw(422, 512 - 158 - 9, 9, 9, kirby.x, kirby.y - 30, kirby.Hp / kirby.MaxHp * 60, 8)
    # 아이템 출력
    UI_image.clip_draw(175, 512 - 98 - 32, 96, 32, 100, 720 - 75, 200, 200 // 3)
    # 경험치 창 출력
    UI_image.clip_draw(374, 512 - 249 - 23, 10, 23, 1280 // 2, 700, 1280, 40)
    UI_image.clip_draw(424, 512 - 189 - 4, 4, 4, 0, 700, (kirby.Exp / kirby.MaxExp) * 1280 * 2, 28)


def handle_events():
    events = get_events()
    kirby.handle_events(events)
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
def pause():
    pass
def resume():
    pass
def Kirby_init_Test(Weapons, kirby):
    newWeapons = Weapon()
    kirby.type = CharaterSelect_state.Type
    newWeapons.name = CharaterSelect_state.Type
    kirby.__init__()
    newWeapons.__init__()
    Weapons.append(newWeapons)
    del CharaterSelect_state.Type
    del newWeapons
