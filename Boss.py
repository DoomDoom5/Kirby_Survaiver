import random
import math
import game_framework
import winsound

from BehaviorTree import BehaviorTree, Selector, Sequence, Leaf
from pico2d import *
import game_world

from game_states import play_state
import enemy


class TargetMarker:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
    def update(self):
        pass

# Boss Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boss Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4


animation_names = ['Attack', 'Dead', 'Idle', 'Walk', 'Runaway']


# 보스
# : IDLE : 랜덤 마커를 설정하고 움직임을 반복
# : ATTACK : 주변에 플레이어가 있으면 속도가 빨라지고 플레이어를 찾아옴
# : Runaway : 자신의 HP% 가 플레이어보다 낮으면 도망침 (2회 제한)=> 일정 시간 이후 IDLE 상태로 돌아옴
class Boss:
    images = None

    def load_images(self):
        if Boss.images == None:
            Boss.images = load_image("assets/img/Enemy/Normal_game_Enemy.png")

    def __init__(self):
        #self.x, self.y = 1280 / 4 * 3, 1024 / 4 * 3
        self.x, self.y = random.randint(100, 1180), random.randint(100, 924)
        self.tx, self.ty = random.randint(100, 1180), random.randint(100, 924)
        self.load_images()
        self.dir = random.random()*2*math.pi # random moving direction
        self.speed = 0
        self.timer = 1.0 # change direction every 1 sec when wandering
        self.frame = 0.0
        self.build_behavior_tree()

        self.hp = 0

        self.width = 100.
        self.height = 100
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
        return (a.x-b.x)**2 + (a.y-b.y)**2

    def move_to_Kirby(self):
        # fill here
        distance = self.calculate_squared_distance(self,play_state.kirby)
        if distance > (PIXEL_PER_METER * 10) ** 2:
            self.speed = 0
            return BehaviorTree.FAIL
        if self.hp > play_state.kirby.hp:
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

    def flee_from_boy(self):
        # fill here
        distance = self.calculate_squared_distance(self, play_state.kirby)
        if distance > (PIXEL_PER_METER * 10) ** 2:
            self.speed = 0
            return BehaviorTree.FAIL
        if self.hp <= play_state.kirby.hp:
            self.dir = math.atan2(self.y - play_state.kirby.y, self.x - play_state.kirby.x)
            self.speed = RUN_SPEED_PPS
            return BehaviorTree.RUNNING
        else:
            self.speed = 0
            return BehaviorTree.FAIL
        pass


    def build_behavior_tree(self):
        find_random_location_node = Leaf('Find Random Location', self.find_random_location)
        move_to_node = Leaf('Move To', self.move_to)

        wander_sequence = Sequence('Wander', find_random_location_node, move_to_node)

        move_to_node = Leaf('Move to Boy', self.move_to_boy)
        flee_from_boy_node = Leaf('Flee from Boy', self.flee_from_boy)
        chase_or_flee_selector = Selector('Chase or Flee Boy', move_to_node, flee_from_boy_node)

        final_selector = Selector('Final', chase_or_flee_selector, wander_sequence)
        self.bt = BehaviorTree(final_selector)


    def get_bb(self):
        return self.sx - self.width//2, self.sy - self.width//2, self.sx + self.height//2, self.sy + self.height//2

    def update(self):
        # fill here
        self.bt.run()
        self.calculate_current_position()

    def draw(self):
        #fill here
        if math.cos(self.dir) < 0:
            if self.speed == 0:
                #Boss.images['Idle'][int(self.frame)].draw(self.x, self.y, 100, 100)
                self.image.clip_composite_draw(int(self.frame) * 70, 1190 - 336 - 63, 63, 63,
                                               0, 'h', sx, sy, self.width, self.height)
            else:
                #Boss.images['Walk'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
                self.image.clip_composite_draw(int(self.frame) * 70, 1190 - 336 - 63, 63, 63,
                                               0, 'h', sx, sy, self.width, self.height)
        else:
            if self.speed == 0:
                self.image.clip_composite_draw(int(self.frame) * 70, 1190 - 336 - 63, 63, 63,
                                               0, '', sx, sy, self.width, self.height)
            else:
                self.image.clip_composite_draw(int(self.frame) * 70, 1190 - 336 - 63, 63, 63,
                                               0, '', sx, sy, self.width, self.height)

    def handle_event(self, event):
        pass

    def handle_collision(self, other, group):
        pass
