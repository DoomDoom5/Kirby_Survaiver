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

#1 : 이벤트 정의
RD, LD, TD, BD ,RU, LU, TU, BU, RTD, RTU ,TIMER, SPACE = range(12)
event_name = ['RD', 'LD','TD','BD' ,'RU', 'LU', 'TU' , 'BU', 'RTD' , 'RTU' ,'TIMER', 'SPACE']

#2 : 상태의 정의
class IDLE:
    def enter(self,event):
        print('ENTER IDLE')
        self.x_dir = 0
        self.y_dir = 0

    def exit(self, event):
        print('EXIT IDLE')

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
    def draw(self):
        print("IDLE그림")
        if self.invers == False:
            self.image.clip_composite_draw(int(self.frame) * 34, 616 - 80, 33, 37,
                                           0, '', self.x, self.y ,self.width, self.height)
        else:
            self.image.clip_composite_draw(int(self.frame) * 34, 616 - 80, 33, 37,
                                           0, 'h', self.x, self.y ,self.width, self.height)
class RUN:
    def enter(self, ):
        print('ENTER RUN')





    def exit(self, event):
        print('EXIT RUN')

    def do(self, MapEndLeft = 0, MapEndRight = 1280, MapEndBottom = 720, MapEndTop = 0):
        dgree = 0.0
        if self.x_dir == 0 and self.y_dir == 0:
            pass
        if self.x_dir > 0:
            if self.y_dir > 0:  # 둘다 dir이 1 -> 45도
                dgree = 45.0
            elif self.y_dir < 0:
                dgree = 315.0
            else:
                dgree = 0.0
            pass
        elif self.x_dir < 0:
            if self.y_dir > 0:
                dgree = 135.0
            elif self.y_dir < 0:
                dgree = 225.0
            else:
                dgree = 180.0
            pass
        elif self.x_dir == 0:
            if self.y_dir > 0:
                dgree = 90.0
            elif self.y_dir < 0:
                dgree = 270.0

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) %7
        self.x += math.cos(math.radians(dgree)) * RUN_SPEED_PPS * game_framework.frame_time * self.speed
        self.x = clamp(0, self.x, 1280)
        self.y += math.sin(math.radians(dgree)) * RUN_SPEED_PPS * game_framework.frame_time * self.speed
        self.y = clamp(0, self.y, 720)

        pass

        # self.x = clamp(0, self.x, 1600)

    def draw(self):
        if self.invisivleTime > 0.0 and int(self.frame)%2 == 0:
            pass
        else:
            if self.invers == False:
                self.image.clip_composite_draw(114 + int(self.frame) * 33, 616 - 80, 33, 34,
                                               0, '', self.x, self.y, self.width, self.height)
            elif self.invers == True:
                self.image.clip_composite_draw(114 + int(self.frame) * 33, 616 - 80, 33, 34,
                                               0, 'h', self.x, self.y, self.width, self.height)


#3. 상태 변환 구현

next_state = {
    IDLE:  {RU: RUN,  LU: RUN,  TU: RUN , BU : RUN, RD: RUN,  LD: RUN,  TD: RUN , BD : RUN, RTD : RUN, RTU : RUN},
    RUN:   {RU: IDLE,  LU: IDLE,  TU: IDLE , BU : IDLE, RD: IDLE,  LD: IDLE,  TD: IDLE , BD : IDLE, RTD : IDLE, RTU : IDLE}
}


# 캐릭터가 가져야 할것
class Player:
    image = None
    effect_Image = None
    weapons = set()
    type = None
    width = 40
    height = 40
    Attack = 0

    MaxHp = 100.0  # 최대 Hp
    Hp = MaxHp  # 현재 HP

    Maxgauge = 100
    gauge = 0

    MaxExp = 5
    Exp = 0
    Level = 0
    Defence = 0.0  # 방어력
    Recovery = 0.05  # 재생력
    BulletSpeed = 1.0  # 투사채 속도
    BulletRange = 1.0  # 투사채 크기
    BulletNum = 1  # 추가 투사체 수
    Luck = 0.0  # 운에 따라 선택지 4개
    Magent = 0.0  # 경험치 흡수 범위
    Revival = 0  # 부활 횟수

    def __init__(self):
        self.Magent = 100.0
        if self.type == "ICE":
            self.image = load_image("assets/img/Kirby/Ice_Kirby_empty.png")
        elif self.type == "FIRE":
            self.image = load_image("assets/img/Kirby/Fire_Kirby_empty.png")
        elif self.type == "PLASMA":
            self.image = load_image("assets/img/Kirby/PLASMA_Kirby_empty.png")

        self.speed = 1
        self.x, self.y = 1280//2, 720//2
        self.frame = 0
        self.x_dir, self.y_dir, self.invers = 0, 0,True

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)
        pass

    def get_bb(self):
        return self.x - self.width//2, self.y - self.height//2, self.x + self.width//2, self.y + self.height//2

    def check_Enemy_Coll(self, enemy_Attack):
        print("충돌!")
        if self.invisivleTime <= 0:
            self.Hp -= enemy_Attack
            self.invisivleTime = self.Max_invisivleTime
        pass
    def draw(self):
        self.cur_state.draw(self)
        pass

    def add_event(self, event):
        self.event_que.insert(0, event)

    def Attack_Weapons(self):
        for weapons in self.weapons:
            weapons.Attack()
            pass

    def update(self):

        pass


