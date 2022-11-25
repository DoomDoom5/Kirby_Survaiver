from pico2d import *
import game_framework
import math

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
    weapons = ()
    MaxHp = 100.0  # 최대 Hp
    Hp = MaxHp  # 현재 HP

    Defence = 0.0  # 방어력
    Recovery = 0.05  # 재생력
    BulletSpeed = 1.0  # 투사채 속도
    BulletRange = 1.0  # 투사채 크기
    BulletNum = 1  # 추가 투사체 수

    def __init__(self, element):
        self.Magent = 100.0
        if element == "ICE":
            self.image = load_image("assets/img/Kirby/Ice_Kirby_empty.png")
        elif element == "FIRE":
            self.image = load_image("assets/img/Kirby/Fire_Kirby_empty.png")
        elif element == "PLASMA":
            self.image = load_image("assets/img/Kirby/PLASMA_Kirby_empty.png")

        self.speed = 1
        self.x, self.y = 1280//2, 720//2
        self.frame = 0
        self.x_dir, self.y_dir, self.invers = 0, 0,True
        self.dgree = 0
        self.state = "IDLE"
        pass

    def get_bb(self):
        return self.x - self.width//2, self.y - self.height//2, self.x + self.width//2, self.y + self.height//2

    def draw(self):
        if self.x_dir == 0 and self.y_dir == 0:
            if self.invers == False:
                self.image.clip_composite_draw(int(self.frame) * 34, 616 - 80, 33, 37,
                                               0, '', self.x, self.y, self.width, self.height)
            else:
                self.image.clip_composite_draw(int(self.frame) * 34, 616 - 80, 33, 37,
                                               0, 'h', self.x, self.y, self.width, self.height)
            pass
        elif self.x_dir == 0 and self.y_dir == 0:
            if self.invers == False:
                self.image.clip_composite_draw(114 + int(self.frame) * 33, 616 - 80, 33, 34,
                                               0, '', self.x, self.y, self.width, self.height)
            elif self.invers == True:
                self.image.clip_composite_draw(114 + int(self.frame) * 33, 616 - 80, 33, 34,
                                               0, 'h', self.x, self.y, self.width, self.height)

        pass


    def update(self, player_x , player_y):
        if self.x > player_x:
            self.invers = True
            self.x_dir = -1
        else :
            self.invers = False
            self.x_dir = +1

        if self.y > player_y:
            self.y_dir = -1
        else:
            self.y_dir = 1
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 7
        self.x += math.cos(math.radians(self.dgree)) * RUN_SPEED_PPS * game_framework.frame_time * self.speed
        self.x = clamp(0, self.x, 1280)
        self.y += math.sin(math.radians(self.dgree)) * RUN_SPEED_PPS * game_framework.frame_time * self.speed
        self.y = clamp(0, self.y, 720)
        pass


