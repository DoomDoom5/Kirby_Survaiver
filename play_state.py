from pico2d import *
import game_framework
import random
import CharaterSelect_state
import mapSelect_state
import levelUp_state

from map import Map
from Character import Player
from enemy import  Enemy
from Manager.Item_Manager import Missile_manager
from Manager.Item_Manager import Weapon
from Manager.Item_Manager import Item_manager
from Manager.Ui_Manager import Item_UI_Manager


filld = None

missile_manager = None
item_manager = Item_manager()
item_UI_Manager = Item_UI_Manager()
Weapons = []

max_col = 40
max_row = 40

kirby = Player()
UI_image = None
Enemys = None
Timer = 0
fps = 0.01
enemy_responTimer = 0
gameMap = None

def enter():
    global tiles, kirby, Enemys, UI_image, Weapons,item_manager,gameMap, Enemys, missile_manager
    missile_manager = Missile_manager()

    UI_image = load_image("assets/Ui/UI.png")

    item_manager.Items_image = load_image("assets/Ui/items.png")

    Enemys = [Enemy() for i in range(0, 10)]
    Kirby_init_Test(Weapons, kirby)

    gameMap = Map(mapSelect_state.Type)

    for s_Enemy in Enemys :
        r = random.randint(0,2)
        s_Enemy.name = "Waddle_dee"
        s_Enemy.__init__()
        if r == 0:
            s_Enemy.x = random.randint(1280,1290)
        elif r == 1 :
            s_Enemy.x = random.randint(-10, 0)
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


    if enemy_responTimer >= 2.0:
        newEnemy = Enemy()
        r = random.randint(0,2)
        if Timer > 5.0:
            newEnemy.name = "kinght"
            newEnemy.__init__()
        else:
            newEnemy.name = "Waddle_dee"
            newEnemy.__init__()
        if r == 0:
            newEnemy.x = random.randint(1280,1290)
        elif r ==1 :
            newEnemy.x = random.randint(-10, 0)
        Enemys.append(newEnemy)
        del newEnemy
        enemy_responTimer = 0
    else:
        enemy_responTimer += fps
    pass


def Kriby_Update():
    kirby.Move()
    kirby.Exp += item_manager.GainExp(kirby.x, kirby.y, kirby.Magent, kirby.Exp)
    if(kirby.levelUP()):
        game_framework.push_state(levelUp_state)
        pass


def draw():
    global Timer
    clear_canvas()

    if gameMap.image != None:
        gameMap.draw(kirby.x, kirby.y)
    for s_Enemy in Enemys:
        s_Enemy.draw()
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

def MapMovement():
    pass


