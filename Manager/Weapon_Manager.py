import random
from pico2d import *
import game_framework
import game_world
import math
import server
from game_states import play_state

# weapon Run Speed
PIXEL_PER_METER = (10.0/0.4)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# weapon Action Speed
TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 16
class Missile:
    # ICE, FIRE, HAMMER 등등등
    name = "None"
    # state = 0 : 발사중, 1 : 파괴, 2 : 소멸
    state = None
    image = None
    x = 0
    y = 0
    sx = 0
    sy = 0
    x_dir = 0

    level = 1 # 레벨

    width = 0 # 너비
    height = 0 # 크기

    Attack = 0 # 공격력
    BulletSpeed = 1.0  # 투사채 속도
    BulletRange = 1.0  # 투사채 크기
    BulletNum = 1  # 추가 투사체 수

    DurationTime = 0

    def get_bb(self):
        return self.sx - self.width // 2, self.sy - self.height // 2, self.sx + self.width // 2, self.sy + self.height // 2

    def Check_Hit_Enemy(self):
        if self.state == 0:
            if self.name != "PLASMA":
                self.state = 1

class ICE(Missile): # 가로로 일직선 공격
    coolTimer = 2
    def __init__(self, level=0, invers=False,charater_x = 0,charater_y = 0,charater_Attack = 0, shoter = 0):
        self.frame = 0
        self.state = 0
        self.width = 30
        self.height = 30
        self.BulletRange = 1.0
        self.BulletSpeed = 5.0  # 투사채 속도
        self.Attack = 10 + charater_Attack
        self.x = charater_x
        self.y = charater_y

        if invers:
            self.x_dir = 1
        else:
            self.x_dir = -1
            pass

        for i in range(0,level):
            self.width *= 1.3
            self.height *= 1.3
            self.BulletSpeed +=0.3  # 투사채 속도
            self.Attack *= 1.4
            pass

        # if level >= 1:
        #     pass
        # if level >= 2:
        #     pass
        # if level >= 3:
        #     pass

    def update(self, player_x, player_y):
        self.sx, self.sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        if self.state == 0:
            self.x += self.x_dir * self.BulletSpeed * RUN_SPEED_PPS * game_framework.frame_time
            if self.sx > server.background.w:
                self.frame = 0
                self.state = 1
            elif self.sx < 0:
                self.frame = 0
                self.state = 1

        if self.state == 1:
            if self.frame > 4:
                self.state = 2

    def draw(self, image):
        if self.state == 0:
            draw_rectangle(*self.get_bb())
            image.clip_draw(365, 552-45 - 24, 24,24,self.sx, self.sy, self.width * self.BulletRange, self.height * self.BulletRange)
        if self.state == 1:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)
            match int(self.frame):
                case 0 :
                    image.clip_draw(245, 552-19 - 16, 20,20, self.sx, self.sy,self.width * 2 * self.BulletRange,self.height * 2 * self.BulletRange)
                case 1 :
                    image.clip_draw(265, 552-19 - 16, 20,20, self.sx, self.sy,self.width * 2 * self.BulletRange,self.height * 2 * self.BulletRange)
                case 2 :
                    image.clip_draw(291, 552-19 - 16, 30,30, self.sx, self.sy,self.width  * 2* self.BulletRange,self.height * 2 * self.BulletRange)
                case 3 :
                    image.clip_draw(335, 552-19 - 16, 30,30, self.sx, self.sy,self.width * 2 * self.BulletRange,self.height * 2 * self.BulletRange)
                case 4 :
                    image.clip_draw(373, 552-19 - 16, 30,30, self.sx, self.sy,self.width * 2 * self.BulletRange,self.height * 2 * self.BulletRange)
        pass



class FIRE(Missile): # 무작위 발사
    coolTimer = 4
    def __init__(self, level=0, invers=False,charater_x = 0,charater_y = 0,charater_Attack = 0, shoter = 0):
        self.frame = 0
        self.state = 0
        self.width = 58
        self.height = 30
        self.BulletSpeed = 5.0  # 투사채 속도
        self.Attack = 20 + charater_Attack
        self.x = charater_x
        self.y = charater_y
        self.dgree = random.randint(0,359)
        self.DurationTime = 4.0
        if invers:
            self.x_dir = 1
        else:
            self.x_dir = -1
            pass
        self.x += self.x_dir * 10
        for i in range(0,level):
            self.width *= 1.3
            self.height *= 1.3
            self.BulletSpeed += 0.3  # 투사채 속도
            self.Attack *= 1.3
            pass

    def update(self, player_x, player_y):
        self.sx, self.sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        if self.state == 0:
            self.x += (math.cos(self.dgree)) * self.BulletSpeed * RUN_SPEED_PPS * game_framework.frame_time
            self.y += (math.sin(self.dgree) ) * self.BulletSpeed * RUN_SPEED_PPS * game_framework.frame_time
            if self.x > server.background.w or self.x < 0 or self.y >  server.background.h or self.y < 0:
                self.state = 1
        elif self.state == 1:
            if self.frame > 4:
                self.state = 2

    def draw(self, image):
        if self.state == 0:
            draw_rectangle(*self.get_bb())
            image.clip_composite_draw(337, 552-424-15, 29, 15,
                                            self.dgree, ' ', self.sx, self.sy, self.width , self.height * self.BulletRange)
        if self.state == 1:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)
            match int(self.frame):
                case 0 :
                    image.clip_draw(88, 552-19 - 20, 20,20,self.sx, self.sy,self.width  ,self.height)
                case 1 :
                   image.clip_draw(88, 552-19 - 20, 20,20,self.sx, self.sy,self.width  ,self.height )
                case 2 :
                   image.clip_draw(88, 552-19 - 30, 30,30,self.sx, self.sy,self.width,self.height  )
                case 3 :
                    image.clip_draw(88, 552-19 - 30, 30,30,self.sx, self.sy,self.width ,self.height )
                case 4 :
                   image.clip_draw(88, 552-19 - 30, 30,30,self.sx, self.sy,self.width  ,self.height)
        pass


class PLASMA(Missile):
    coolTimer = 3
    def __init__(self, level=0, invers=False, charater_x = 0,charater_y = 0,charater_Attack = 0, shoter = 0):
        self.frame = 0
        self.state = 0
        self.width = 30
        self.height = 30
        self.BulletRange = 1.0
        self.BulletSpeed = 3.0  # 투사채 속도
        self.Attack = (5 + charater_Attack)/5
        self.dgree = random.randint(0,359)
        self.x = charater_x
        self.y = charater_y
        self.DurationTime = 3.0
        self.shoter = shoter

        for i in range(0,level):
            self.width *= 1.3
            self.height *= 1.3
            self.BulletSpeed += 0.3  # 투사채 속도
            self.Attack *= 1.3
            pass

        if level == 1:
            pass
        elif level == 2:
            pass
        elif level == 3:
            pass
    def update(self, player_x, player_y):
        if self.state == 0:
            self.dgree = self.dgree + self.BulletSpeed * RUN_SPEED_PPS * game_framework.frame_time
            self.DurationTime -= game_framework.frame_time
            if self.shoter == 0:
                self.sx = play_state.kirby.sx + math.cos(math.radians(self.dgree)) * self.BulletSpeed * 40
                self.sy = play_state.kirby.sy + math.sin(math.radians(self.dgree)) * self.BulletSpeed * 40
                if self.DurationTime <= 0:
                    self.state = 2
                    del self

            elif self.shoter == 1:
                self.sx = play_state.kirby_partner_1.sx + math.cos(math.radians(self.dgree)) * self.BulletSpeed * 10
                self.sy = play_state.kirby_partner_1.sy + math.sin(math.radians(self.dgree)) * self.BulletSpeed * 10
                if self.DurationTime <= 0:
                    self.state = 2
                    del self

            elif self.shoter == 2:
                self.sx = play_state.kirby_partner_2.sx + math.cos(math.radians(self.dgree)) * self.BulletSpeed * 10
                self.sy = play_state.kirby_partner_2.sy + math.sin(math.radians(self.dgree)) * self.BulletSpeed * 10
                if self.DurationTime <= 0:
                    self.state = 2
                    del self

    def draw(self, image):
        draw_rectangle(*self.get_bb())
        if self.state == 0:
            image.clip_composite_draw(264, 552-44-16, 17, 16, 0, ' ', self.sx, self.sy, self.width * self.BulletRange, self.height * self.BulletRange)
            draw_rectangle(*self.get_bb())
        pass


class Missile_manager:
    missiles = []
    ice = ICE()
    fire = FIRE()
    plasma = PLASMA()
    image = None

    def __init__(self):
        if Missile_manager.image == None:
            Missile_manager.image = load_image("assets/img/Effect/vfx.png")

    def draw(self):
        for missile in self.missiles:
            if missile.name == "ICE":
                self.ice = missile
                self.ice.draw(self.image)

            elif missile.name == "FIRE":
                self.fire = missile
                self.fire.draw(self.image)

            elif missile.name == "PLASMA":
                self.plasma = missile
                self.plasma.draw(self.image)
                pass

    def update(self, player_x, player_y):
        for missile in self.missiles:
            if missile.state == 2:
                self.missiles.remove(missile)
            elif missile.name == "ICE":
                self.ice = missile
                self.ice.update(player_x, player_y)
            elif missile.name == "FIRE":
                self.fire = missile
                self.fire.update(player_x, player_y)
            elif missile.name == "PLASMA":
                self.plasma = missile
                self.plasma.update(player_x, player_y)
        pass


class Weapon:
    name= None
    shotTimer = 0.0
    level = 1
    shotOn = None
    def __init__(self,name):
        self.name = name
        self.shotTimer = 0
        pass

    def shot(self, charater_x, charater_y,charater_Attack  ,charater_invers, missile_manager, shoter=0):
        # shoter = 0:플레이어 , 1 : 파트너1 , 2 : 파트너2
        self.shotTimer += game_framework.frame_time
        if self.name == None:
            return
        self.shotOn = False
        new_missile = None

        if self.name == "ICE":
            if self.shotTimer >= ICE.coolTimer:
                new_missile = ICE()
                self.shotOn = True
                self.shotTimer = 0.0

        elif self.name == "FIRE":
            if self.shotTimer >= FIRE.coolTimer:
                print("발사")
                new_missile = FIRE()
                self.shotOn = True
                self.shotTimer = 0.0

        elif self.name == "PLASMA":
            if self.shotTimer >= PLASMA.coolTimer:
                new_missile = PLASMA()
                self.shotOn = True
                self.shotTimer = 0.0

            pass

        if self.shotOn == True:
            self.shotOn = False
            new_missile.name = self.name
            new_missile.__init__(self.level, charater_invers, charater_x, charater_y, charater_Attack, shoter)
            missile_manager.missiles.append(new_missile)
            del new_missile

