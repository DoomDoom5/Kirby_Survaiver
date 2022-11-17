from pico2d import *
import game_framework
import random
import CharaterSelect_state
import game_world
import mapSelect_state
import levelUp_state

from map import Map
from Character import Player
from enemy import  Enemy
from Manager.Item_Manager import Missile_manager
from Manager.Item_Manager import Weapon
from Manager.Item_Manager import Item_manager
from Manager.Ui_Manager import UI_Manager


filld = None

missile_manager = None
item_manager = None
ui_Manager = None
Weapons = []

max_col = 40
max_row = 40

kirby = None
Enemys = None
Timer = 0
fps = 0.01
enemy_responTimer = 0
gameMap = None

def enter():
    global tiles, kirby, Enemys, Weapons,item_manager,gameMap, Enemys, missile_manager, ui_Manager,kirby

    missile_manager = Missile_manager()

    ui_Manager = UI_Manager()
    item_manager = Item_manager()

    game_world.add_object(ui_Manager, 2)
    game_world.add_object(item_manager, 2)


    Enemys = [Enemy() for i in range(0, 10)]
    ui_Manager.Weapons.append("ICE")

    kirby = Player()
    Kirby_init_Test(Weapons, kirby)
    game_world.add_object(kirby,1)

    gameMap = Map(mapSelect_state.Type)
    game_world.add_object(gameMap,0)

    for s_Enemy in Enemys :
        r = random.randint(0,2)
        s_Enemy.name = "Waddle_dee"
        s_Enemy.__init__()
        if r == 0:
            s_Enemy.x = random.randint(1280,1290)
        elif r == 1 :
            s_Enemy.x = random.randint(-10, 0)
        game_world.add_object(s_Enemy, 1)
        pass

def exit():
    pass

def update():
    global enemy_responTimer, Timer
    if kirby.invisivleTime > 0 :
        kirby.invisivleTime -= fps
    missile_manager.Move()

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
        game_world.add_object(newEnemy, 1)
        Enemys.append(newEnemy)
        del newEnemy
        enemy_responTimer = 0
    else:
        enemy_responTimer += fps
    pass

    for game_object in game_world.all_objects():
        game_object.update() # game_world에서 제너레이터 하였기 때문에

    Kriby_Update()

def Kriby_Update():
    kirby.Move()
    kirby.Exp += item_manager.GainExp(kirby.x, kirby.y, kirby.Magent, kirby.Exp)
    ui_Manager.player_UI_update(kirby.x, kirby.y, kirby.Hp, kirby.MaxHp, kirby.Exp, kirby.MaxExp)

    if(kirby.levelUP()):
        game_framework.push_state(levelUp_state)
        pass



def draw():
    global Timer
    clear_canvas()
    draw_world()

    missile_manager.draw()

    update_canvas()
    Timer += fps
    delay(fps)
    # fill here
    pass

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw() # game_world에서 제너레이터 하였기 때문에
    pass

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


