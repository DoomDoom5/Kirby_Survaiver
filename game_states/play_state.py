from pico2d import *
from game_states import CharaterSelect_state
from game_states import mapSelect_state
from game_states import game_end_state
from game_states import special_attack_state
import server
import game_framework
import game_world

from map import Map
from Character import Player
from enemy import Enemy
from partner import Partner
from Manager.Weapon_Manager import Missile_manager
from Manager.Item_Manager import Item_manager
from Manager.Ui_Manager import UI_Manager
from Manager.Ui_Manager import enemy_Demage_Draw

missile_manager = None
item_manager = None

kirby = None
kirby_partner_1 = None
kirby_partner_2 = None

createBoss = False
game_clear = False

Enemys = None
Timer = None
enemy_responTimer = None

def enter():
    global  kirby, Enemys,item_manager, missile_manager, kirby_partner_1,kirby_partner_2,Timer, enemy_responTimer,game_clear
    Timer = 0
    enemy_responTimer = 0
    game_clear = False
    server.background = Map(mapSelect_state.Type)
    game_world.add_object(server.background,0)

    missile_manager = Missile_manager()
    server.ui_Manager = UI_Manager()
    server.ui_Manager.Weapons.append(CharaterSelect_state.Type)
    item_manager = Item_manager()

    game_world.add_object(missile_manager,2)
    game_world.add_object(server.ui_Manager, 3)
    game_world.add_object(item_manager, 2)

    kirby = Player(CharaterSelect_state.Type)
    game_world.add_object(kirby,1)

    kirby_partner_1 = Partner(CharaterSelect_state.subType_1, 1)
    kirby_partner_1.x = 1280//2 - 40
    game_world.add_object(kirby_partner_1, 1)
    del CharaterSelect_state.subType_1

    kirby_partner_2 = Partner(CharaterSelect_state.subType_2, 2)
    kirby_partner_2.x = 1280//2 + 40
    game_world.add_object(kirby_partner_2, 1)
    del CharaterSelect_state.subType_2



    Enemys = [Enemy("Waddle_dee") for i in range(0, 10)]
    for s_Enemy in Enemys :
        game_world.add_object(s_Enemy, 1)
        pass



def exit():
    global kirby, Enemys, item_manager, missile_manager, createBoss, game_clear, Timer, enemy_responTimer, kirby_partner_1,kirby_partner_2, game_world
    del kirby, Enemys, item_manager, missile_manager, createBoss, game_clear, Timer, enemy_responTimer, kirby_partner_1,kirby_partner_2, game_world
    pass

def update():
    global Timer,enemy_responTimer,s_Enemy
    Timer += game_framework.frame_time
    server.ui_Manager.elapsed_time += game_framework.frame_time

    for s_Enemy in Enemys :
        for s_missile in missile_manager.missiles:
            if collide(s_Enemy, s_missile) == True and s_missile.state == 0:
                s_Enemy.hit_sound.play(1)
                s_Enemy.On_damege(s_missile.Attack)
                game_world.add_object(enemy_Demage_Draw(s_Enemy.sx, s_Enemy.sy, s_Enemy.height, s_missile.Attack),3)
                s_missile.Check_Hit_Enemy()
        if s_Enemy.Hp <= 0 :
            s_Enemy.dead_sound.play(1)
            item_manager.Create_EXP_Stone(s_Enemy.crystal, s_Enemy.x, s_Enemy.y)
            game_world.remove_object(s_Enemy)
            Enemys.remove(s_Enemy)
            server.ui_Manager.kill_Enemy += 1

        if abs(kirby.x - s_Enemy.x) < 80 or abs(kirby.y - s_Enemy.y) < 80:
            if collide(kirby, s_Enemy):
                kirby.check_Enemy_Coll(s_Enemy.power)

    if enemy_responTimer > 2:
        enemy_responTimer = 0
        Enemy.spawnEnemy(Timer, Enemys)
    else :
        enemy_responTimer += game_framework.frame_time

    for game_object in game_world.all_objects():
        game_object.update(kirby.x, kirby.y) # game_world에서 제너레이터 하였기 때문에

    if game_clear == True:
        game_framework.push_state(game_end_state)
    elif kirby.HP <= 0:
        game_framework.push_state(game_end_state)



def draw():
    clear_canvas()
    draw_world()
    update_canvas()
    pass

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw() # game_world에서 제너레이터 하였기 때문에
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        kirby.handle_events(event)

def pause():
    pass
def resume():
    pass

def collide(a,b):
    left_a , bottom_a , right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True
