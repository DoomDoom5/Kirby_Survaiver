from pico2d import *
import game_framework
import math
from game_states import play_state
from enemy import Enemy
from Manager.Weapon_Manager import Weapon
import game_world
import server

# Kriby Run Speed
PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Kriby Action Speed
TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

# 캐릭터가 가져야 할것
class Partner:
    image = None
    width = 40
    height = 40
    Attack = 0
    weapons = []

    Defence = 0.0  # 방어력
    Recovery = 0.05  # 재생력
    BulletSpeed = 1.0  # 투사채 속도
    BulletRange = 1.0  # 투사채 크기
    BulletNum = 1  # 추가 투사체 수

    def __init__(self, element, helper_num):
        if element == "ICE":
            self.speed = 0.3
            self.image = load_image("assets/img/Kirby/Ice_Kirby_empty.png")
        elif element == "FIRE":
            self.speed = 0.5
            self.image = load_image("assets/img/Kirby/Fire_Kirby_empty.png")
        elif element == "PLASMA":
            self.speed = 0.6
            self.image = load_image("assets/img/Kirby/PLASMA_Kirby_empty.png")

        self.x, self.y = 1280//2, 720//2
        self.frame = 0
        self.dir, self.invers = 0,True
        self.dgree = 0
        self.target_enemy = None
        self.helper_num = helper_num

        self.get_Weapon(element)

        pass

    def get_bb(self):
        return self.x - self.width//2, self.y - self.height//2, self.x + self.width//2, self.y + self.height//2
    def get_Weapon(self, name):
        self.weapons.append(Weapon(name))
        pass
    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom

        if self.dir == 0:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
            if self.invers == False:
                self.image.clip_composite_draw(int(self.frame) * 34, 616 - 79, 33, 37,
                                               0, '',sx, sy, self.width, self.height)
            else:
                self.image.clip_composite_draw(int(self.frame) * 34, 616 - 79, 33, 37,
                                               0, 'h', sx, sy, self.width, self.height)
            pass
        else:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 7
            if self.invers == False:
                self.image.clip_composite_draw(114 + int(self.frame) * 33, 616 - 78, 33, 34,
                                               0, '', sx, sy, self.width, self.height)
            elif self.invers == True:
                self.image.clip_composite_draw(114 + int(self.frame) * 33, 616 - 78, 33, 34,
                                               0, 'h', sx, sy, self.width, self.height)
        pass

    def Attack_Weapons(self):
        for weapon in self.weapons:
            sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
            weapon.shot(self.x, self.y, self.Attack, self.invers, play_state.missile_manager, self.helper_num)
            pass


    def update(self, player_x , player_y):
        self.Attack_Weapons()

        if server.partner1.target_enemy == server.partner2.target_enemy and self.target_enemy != None:
            self.find_enemy_location()
            return

        if self.target_enemy == None:
            if self.x > player_x:
                self.invers = False
            else:
                self.invers = True

            if abs(player_y - self.y) < 80 and abs(player_x - self.x) < 80:
                return
            self.dir = math.atan2(player_y - self.y, player_x - self.x)
            self.x += math.cos(self.dir) * RUN_SPEED_PPS * game_framework.frame_time * self.speed
            self.x = clamp(0, self.x, 1280)
            self.y += math.sin(self.dir) * RUN_SPEED_PPS * game_framework.frame_time * self.speed
            self.y = clamp(0, self.y, 720)

        else:
            if self.x > self.target_enemy.x:
                self.invers = False
            else:
                self.invers = True

            if abs(self.target_enemy.y - self.y) < 30 and abs(self.target_enemy.x - self.x) < 30:
                return
            self.dir = math.atan2(self.target_enemy.y - self.y, self.target_enemy.x - self.x)



            self.x += math.cos(self.dir) * RUN_SPEED_PPS * game_framework.frame_time * self.speed
            self.x = clamp(self.width//2, self.x, server.background.w- 1 - self.width//2)
            self.y += math.sin(self.dir) * RUN_SPEED_PPS * game_framework.frame_time * self.speed
            self.y = clamp(self.height//2, self.y, server.background.h- 1 - self.height//2)

            pass
        pass

    def find_enemy_location(self):
        self.target_enemy = None
        shortest_distance = 1280**2
        for o in game_world.all_objects():
            if type(o) is Enemy:
                enemy = o
                distance = (enemy.x - self.x) ** 2 + (enemy.y - self.y) ** 2
                if distance < (PIXEL_PER_METER * 10) ** 2 and distance < shortest_distance:
                    self.target_enemy = enemy
                    shortest_distance = distance

                pass
        pass
