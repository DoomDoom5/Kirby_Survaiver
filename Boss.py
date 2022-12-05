import random
import math
import game_framework
import enemy
import server

from BehaviorTree import BehaviorTree, Selector, Sequence, Leaf
from pico2d import *
import game_world

from game_states import play_state


class TargetMarker:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
    def update(self, player_x, player_y):
        pass
    def draw(self):
        pass

# Boss Run Speed
PIXEL_PER_METER = (10.0 / 0.2)  # 10 pixel 20 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boss Action Speed
TIME_PER_ACTION = 4
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4


animation_names = ['Attack', 'Dead', 'Idle', 'Walk', 'Runaway']


# 보스
# : IDLE : 랜덤 마커를 설정하고 움직임을 반복
# : ATTACK : 주변에 플레이어가 있으면 속도가 빨라지고 플레이어를 찾아옴
# : Runaway : 자신의 HP% 가 플레이어보다 낮으면 도망침 (2회 제한)=> 일정 시간 이후 IDLE 상태로 돌아옴
class Boss():
    image = None
    hit_sound = None
    dead_sound = None
    def __init__(self):
        # self.x, self.y = 1280 / 4 * 3, 1024 / 4 * 3
        self.x, self.y = random.randint(100, 1180), random.randint(100, 500)
        self.tx, self.ty = random.randint(100, 1180), random.randint(100, 500)
        self.sx, self.sy  = self.x - server.background.window_left, self.y - server.background.window_bottom
        if Boss.image == None:
            Boss.image = load_image("assets/img/Enemy/Normal_game_Enemy.png")
        if Boss.hit_sound is None:
            Boss.hit_sound = load_wav("assets/sounds/VS_EnemyHit_v06-02.ogg")
        if Boss.dead_sound is None:
            Boss.dead_sound = load_wav("assets/sounds/VS_EnemyDead.ogg")

        self.dir = random.random() * 2 * math.pi  # random moving direction
        self.speed = 0.7
        self.frame = 0.0
        self.build_behavior_tree()
        self.width = 110
        self.height = 110
        self.Hp = 1000
        self.MaxHp = 1000
        self.name = "KingDedede"
        self.power = 10
        self.crystal = "RED"

        self.target_marker = TargetMarker(self.tx, self.ty)
        game_world.add_object(self.target_marker, 1)



    def calculate_current_position(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
        self.x = clamp(50, self.x, 1280 - 50)
        self.y = clamp(50, self.y, 1024 - 50)


    def find_random_location(self):
        self.tx, self.ty = random.randint(50, 1230), random.randint(50, 974)
        self.target_marker.x, self.target_marker.y = self.tx, self.ty
        return BehaviorTree.SUCCESS
        # fill here
        pass

    def move_to(self, radius=0.5):
        distance = (self.tx - self.x) ** 2 + (self.ty - self.y) ** 2
        self.dir = math.atan2(self.ty - self.y, self.tx - self.x)

        if distance < (PIXEL_PER_METER * radius) ** 2:
            self.speed = 0
            return BehaviorTree.SUCCESS
        else:
            self.speed = RUN_SPEED_PPS
            return BehaviorTree.RUNNING


    def calculate_squared_distance(self, a, b):
        return (a.sx-b.sx)**2 + (a.sy-b.sy)**2

    def move_to_Kirby(self):
        # fill here
        distance = self.calculate_squared_distance(self,play_state.kirby)
        if distance > (PIXEL_PER_METER * 10) ** 2:
            self.speed = 0
            return BehaviorTree.FAIL
        if self.Hp/self.MaxHp > play_state.kirby.Hp/play_state.kirby.MaxHp:
            self.dir = math.atan2(play_state.kirby.y - self.y, play_state.kirby.x - self.x)
            if distance < (PIXEL_PER_METER * 0.5) ** 2:
                self.speed = 0
                return BehaviorTree.SUCCESS
            else:
                self.speed = RUN_SPEED_PPS
                return BehaviorTree.RUNNING
        else:
            self.speed = 0
            return BehaviorTree.FAIL
        pass

    def flee_from_kirby(self):
        # fill here
        distance = self.calculate_squared_distance(self, play_state.kirby)
        if distance > (PIXEL_PER_METER * 10) ** 2:
            self.speed = 0
            return BehaviorTree.FAIL
        if self.Hp/self.MaxHp <= play_state.kirby.Hp/play_state.kirby.MaxHp:
            self.dir = math.atan2(self.y - play_state.kirby.y, self.x - play_state.kirby.x)
            self.speed = RUN_SPEED_PPS
            return BehaviorTree.RUNNING
        else:
            self.speed = 0
            return BehaviorTree.FAIL
        pass

    def get_bb(self):
        return self.sx - self.width//2 , self.sy - self.height//2 , self.sx + self.width//2 , self.sy + self.height//2

    def build_behavior_tree(self):
        find_random_location_node = Leaf('Find Random Location', self.find_random_location)
        move_to_node = Leaf('Move To', self.move_to)

        wander_sequence = Sequence('Wander', find_random_location_node, move_to_node)

        move_to_node = Leaf('Move to Boy', self.move_to_Kirby)
        flee_from_kirby_node = Leaf('Flee from Boy', self.flee_from_kirby)
        chase_or_flee_selector = Selector('Chase or Flee Boy', move_to_node, flee_from_kirby_node)

        final_selector = Selector('Final', chase_or_flee_selector, wander_sequence)
        self.bt = BehaviorTree(final_selector)

    def update(self, player_x, player_y):
        self.sx, self.sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        # fill here
        self.bt.run()
        self.calculate_current_position()

    def draw(self):
        draw_rectangle(*self.get_bb())
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        #fill here
        if math.cos(self.dir) < 0:
            if self.speed == 0:
                #Boss.images['Idle'][int(self.frame)].draw(self.x, self.y, 100, 100)
                self.image.clip_composite_draw(int(self.frame) * 70, 1190 - 336 - 63, 63, 63,
                                               0, 'h', self.sx, self.sy, self.width, self.height)
            else:
                #Boss.images['Walk'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
                self.image.clip_composite_draw(int(self.frame) * 70, 1190 - 336 - 63, 63, 63,
                                               0, 'h', self.sx, self.sy, self.width, self.height)
        else:
            if self.speed == 0:
                self.image.clip_composite_draw(int(self.frame) * 70, 1190 - 336 - 63, 63, 63,
                                               0, '', self.sx, self.sy, self.width, self.height)
            else:
                self.image.clip_composite_draw(int(self.frame) * 70, 1190 - 336 - 63, 63, 63,
                                               0, '', self.sx, self.sy, self.width, self.height)

    def handle_event(self, event):
        pass

    def handle_collision(self, other, group):
        pass

    @staticmethod
    def createBoss(Timer, Enemys):
        if not play_state.createBoss and Timer > 0:
            play_state.createBoss = True
            newEnemy = Boss()
            game_world.add_object(newEnemy, 1)
            Enemys.append(newEnemy)