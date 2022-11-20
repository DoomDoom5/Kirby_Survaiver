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
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

#1 : 이벤트 정의
RD, LD, TD, BD ,RU, LU, TU, BU,TIMER, SPACE = range(10)
event_name = ['RD', 'LD','TD','BD' ,'RU', 'LU', 'TU' , 'BU' ,'TIMER', 'SPACE']

key_event_table = {
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYDOWN, SDLK_UP): TD,
    (SDL_KEYDOWN, SDLK_DOWN): BD,

    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYUP, SDLK_UP): TU,
    (SDL_KEYUP, SDLK_DOWN): BU,
}

#2 : 상태의 정의
class IDLE:
    def enter(self,event):
        print('ENTER IDLE')
        self.x_dir = 0
        self.y_dir = 0

    def exit(self, event):
        print('EXIT IDLE')

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
    def draw(self):
        print("IDLE그림")
        if self.invers == False:
            self.image.clip_draw(0 + int(self.frame) * 35, 616 - 80, 35, 33, self.x, self.y, self.width, self.height)
        else:
            self.image.clip_draw(0 + int(self.frame) * 34, 616 - 40, 34, 33, self.x, self.y, self.width, self.height)
class RUN:
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.x_dir += 1
            self.invers = True
        elif event == LD:
            self.x_dir -= 1
            self.invers = False
        if event == TD:
            self.y_dir += 1
        elif event == BD:
            self.y_dir -= 1

        if event == RU:
            self.x_dir -= 1
        elif event == LU:
            self.x_dir += 1
        if event == TU:
            self.y_dir -= 1
        elif event == BU:
            self.y_dir += 1

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

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) %8
        self.x += math.cos(math.radians(dgree)) * RUN_SPEED_PPS * game_framework.frame_time * self.speed
        self.x = clamp(0, self.x, 1280)
        self.y += math.sin(math.radians(dgree)) * RUN_SPEED_PPS * game_framework.frame_time * self.speed
        self.y = clamp(0, self.y, 720)

        pass

        # self.x = clamp(0, self.x, 1600)

    def draw(self):
        if self.invers == False:
            self.image.clip_draw(114 + int(self.frame) * 33, 616 - 80, 33, 33, self.x, self.y, self.width,self.height)
        elif self.invers == True:
            self.image.clip_draw(114 + int(self.frame) * 34, 616 - 40, 34, 33, self.x, self.y, self.width,self.height)


#3. 상태 변환 구현

next_state = {
    IDLE:  {RU: RUN,  LU: RUN,  TU: RUN , BU : RUN, RD: RUN,  LD: RUN,  TD: RUN , BD : RUN},
    RUN:   {RU: IDLE,  LU: IDLE,  TU: IDLE , BU : IDLE, RD: IDLE,  LD: IDLE,  TD: IDLE , BD : IDLE}
}


# 캐릭터가 가져야 할것
class Player:
    image = None
    effect_Image = None
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

    invisivleTime = 0.0  # 무적시간
    Max_invisivleTime = 0.4  # 최대 무적시간

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
        if self.invisivleTime <= 0:
            self.Hp -= enemy_Attack
            self.invisivleTime = self.Max_invisivleTime
        pass
    def draw(self):
        self.cur_state.draw(self)
        pass

    def add_event(self, event):
        self.event_que.insert(0, event)
    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        # for event in events:
        #     if (event.type, event.key) in key_event_table:
        #         key_event = key_event_table[(event.type, event.key)]
        #         self.add_event(key_event)
        #
        #     if event.type == SDL_KEYDOWN:
        #         self.state = "RUN"
        #         if event.key == SDLK_RIGHT:
        #             self.x_dir += 1
        #             self.invers = True
        #         elif event.key == SDLK_LEFT:
        #             self.x_dir -= 1
        #             self.invers = False
        #         elif event.key == SDLK_UP:
        #             self.y_dir += 1
        #         elif event.key == SDLK_DOWN:
        #             self.y_dir -= 1
        #         elif event.key == SDLK_1:
        #             self.Exp = self.MaxExp
        #
        #     elif event.type == SDL_KEYUP:
        #         if event.key == SDLK_RIGHT:
        #             self.x_dir -= 1
        #         elif event.key == SDLK_LEFT:
        #             self.x_dir += 1
        #         elif event.key == SDLK_UP:
        #             self.y_dir -= 1
        #         elif event.key == SDLK_DOWN:
        #             self.y_dir += 1
        #
        #     if self.x_dir == 0 and self.y_dir == 0:
        #         self.state = "IDLE"
        #     pass

    def Attack_Weapons(self):
        for Weapon in self.Weapons:
            Weapon.Attack()
            pass

    def levelUP(self):
        if self.Exp >= self.MaxExp:
            self.Exp = self.Exp - self.MaxExp
            self.MaxExp = self.MaxExp * 1.4
            self.Level +=1
            self.cur_state = IDLE
            self.cur_state.enter(self, None)
            return True
        return False

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}    Event {event_name[event]}')
            self.cur_state.enter(self, event)

        if self.Hp < self.MaxHp:
            self.Hp += self.Recovery
        if self.gauge < self.Maxgauge:
            self.gauge += 1

        pass

    def select_Ability(self, selectMenu):
        if selectMenu == 0:
            # 채력 업
            self.MaxHp += 10
            pass
        elif selectMenu == 1:
            self.Attack += 5

        elif selectMenu == 2:
            self.speed += 0.5

        elif selectMenu == 3:
            pass

    def superAttack(self):
        pass



