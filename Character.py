from pico2d import *
import game_framework
import math
from enemy import Enemy

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
RD, LD, TD, BD ,RU, LU, TU, BU, SPACE = range(9)
event_name = ['RD', 'LD','TD','BD' ,'RU', 'LU', 'TU' , 'BU', 'SPACE']

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
#
# key_event_table = {
#     SDLK_SPACE: SPACE,
#     SDLK_RIGHT: RD,
#     SDLK_LEFT: LD,
#     (SDLK_UP): TD,
#     (SDLK_DOWN): BD,
#
#     (SDLK_RIGHT): RU,
#     (SDLK_LEFT): LU,
#     (SDLK_UP): TU,
#     (SDLK_DOWN): BU,
# }


#2 : 상태의 정의

class RUN:
    @staticmethod
    def enter(Player, event):
        print('ENTER RUN')
        if event == RD:
            Player.x_dir += 1
            Player.invers = True
        elif event == LD:
            Player.x_dir -= 1
            Player.invers = False
        elif event == TD:
            Player.y_dir += 1
        elif event == BD:
            Player.y_dir -= 1

        if event == RU:
            Player.x_dir -= 1
        elif event == LU:
            Player.x_dir += 1
        elif event == TU:
            Player.y_dir -= 1
        elif event == BU:
            Player.y_dir += 1

    @staticmethod
    def exit(Player, event):
        print('EXIT RUN')

    @staticmethod
    def do(Player, MapEndLeft = 0, MapEndRight = 1280, MapEndBottom = 720, MapEndTop = 0):
        dgree = 0.0
        if Player.x_dir == 0 and Player.y_dir == 0:
            return
        if Player.x_dir > 0:
            if Player.y_dir > 0:  # 둘다 dir이 1 -> 45도
                dgree = 45.0
            elif Player.y_dir < 0:
                dgree = 315.0
            else:
                dgree = 0.0
            pass
        elif Player.x_dir < 0:
            if Player.y_dir > 0:
                dgree = 135.0
            elif Player.y_dir < 0:
                dgree = 225.0
            else:
                dgree = 180.0
            pass
        elif Player.x_dir == 0:
            if Player.y_dir > 0:
                dgree = 90.0
            elif Player.y_dir < 0:
                dgree = 270.0

        Player.x += math.cos(math.radians(dgree)) * RUN_SPEED_PPS * game_framework.frame_time * self.speed
        Player.x = clamp(0, Player.x, 1280)
        Player.y += math.sin(math.radians(dgree)) * RUN_SPEED_PPS * game_framework.frame_time * self.speed
        Player.y = clamp(0, Player.y, 720)

        pass

    def draw(self):
        if self.invisivleTime > 0.0 and int(self.frame)%2 == 0:
            pass
        elif self.x_dir == 0 and self.y_dir == 0:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
            if self.invers == False:
                self.image.clip_composite_draw(int(self.frame) * 34, 616 - 80, 33, 37,
                                               0, '', self.x, self.y, self.width, self.height)
            else:
                self.image.clip_composite_draw(int(self.frame) * 34, 616 - 80, 33, 37,
                                               0, 'h', self.x, self.y, self.width, self.height)
        else:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) %7
            if self.invers == False:
                self.image.clip_composite_draw(114 + int(self.frame) * 33, 616 - 80, 33, 34,
                                               0, '', self.x, self.y, self.width, self.height)
            elif self.invers == True:
                self.image.clip_composite_draw(114 + int(self.frame) * 33, 616 - 80, 33, 34,
                                               0, 'h', self.x, self.y, self.width, self.height)


#3. 상태 변환 구현

next_state_table = {
    RUN: {RU: RUN, LU: RUN, RD: RUN, LD: RUN,
                TU: RUN, TD: RUN, BU: RUN, BD: RUN,
                SPACE: RUN}
}


# 캐릭터가 가져야 할것
class Player:
    image = None
    weapons = set()
    width = 50
    height = 50
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
    Magent = 0.0  # 경험치 흡수 범위

    invisivleTime = 0.0  # 무적시간
    Max_invisivleTime = 0.4  # 최대 무적시간

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

        self.event_que = []
        self.cur_state = RUN
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
    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


    def Attack_Weapons(self):
        for weapons in self.weapons:
            weapons.Attack()
            pass

    def levelUP(self):
        if self.Exp >= self.MaxExp:
            self.Exp = self.Exp - self.MaxExp
            self.MaxExp = self.MaxExp * 1.4
            self.Level +=1
            self.cur_state = RUN
            self.cur_state.enter(self, None)
            return True
        return False

    def update(self, x = 0,y = 0):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state_table[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}    Event {event_name[event]}')
            self.cur_state.enter(self, event)

        if self.invisivleTime > 0:
            self.invisivleTime -=  game_framework.frame_time
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


    def handle_collision(self, other, group):
        if 'kirby:s_Enemy' == group:
            self.hp -= other.power
    def superAttack(self):
        pass



