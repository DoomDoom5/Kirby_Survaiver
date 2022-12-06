import random
from pico2d import *
import game_world
import game_framework
import server
from game_states import play_state
# Kriby Run Speed
PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 8.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Kriby Action Speed
TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


MAP_one_Enemy = ["Waddle_dee" ,"kinght","Fighter",   "Mike" ,"NinjaCat", "KingDedede" ]

class Enemy:
    name = None
    image = None
    Hpimage = None
    MaxHp = 0
    power = 0  # 공격력
    crystal = None
    sx = 0
    sy = 0

    def __init__(self, name):
        self.frame = 0
        self.invers = False # 캐릭터 오른쪽, 왼쪽
        if Enemy.image == None:
            Enemy.image = load_image("assets/img/Enemy/Normal_Enemy.png")
            pass
        if Enemy.Hpimage == None:
            Enemy.Hpimage = load_image("assets/Ui/UI.png")
            pass

        randp = random.randint(0,4)

        if randp == 0:
            self.x = random.randint(-10,0)
            self.y = random.randint(0,server.background.h)
        elif randp == 1:
            self.x = random.randint(server.background.w,server.background.w + 10)
            self.y = random.randint(0,server.background.h)
        elif randp == 2:
            self.x = random.randint(0,server.background.w)
            self.y = random.randint(-10,0)
        else:
            self.x = random.randint(0,server.background.w)
            self.y = random.randint(server.background.h,server.background.h+10)

        self.name = name

        # 적 타입을 인덱스화 시켜서 하자 => 나중에 수정
        if self.name == MAP_one_Enemy[0]:
            self.MaxHp = 10
            self.speed = 0.3
            self.width = 26
            self.height = 26
            self.power = 2
            self.crystal = "GREEN"


        elif self.name == MAP_one_Enemy[1]:
            self.MaxHp = 20
            self.speed = 0.3
            self.width = 30
            self.height = 30
            self.power = 3
            self.crystal = "BLUE"

        elif self.name == MAP_one_Enemy[2]:
            self.MaxHp = 25
            self.speed = 0.5
            self.width = 35
            self.height = 35
            self.power = 4
            self.crystal = "RED"

        elif self.name ==MAP_one_Enemy[3]:
            self.MaxHp = 40
            self.speed = 0.5
            self.width = 40
            self.height = 40
            self.power = 10
            self.crystal = "RED"

        elif self.name == MAP_one_Enemy[4]:
            self.MaxHp = 80
            self.speed = 0.7
            self.width = 60
            self.height = 40
            self.power = 8
            self.crystal = "RED"

        elif self.name == MAP_one_Enemy[5]:
            self.MaxHp = 400
            self.speed = 0.8
            self.width = 100
            self.height = 100
            self.power = 20
            self.crystal = "GOLD"

        self.Hp = self.MaxHp

    def On_damege(self, charater_Attack):
        self.Hp = self.Hp - charater_Attack

    def draw(self):
        draw_rectangle(*self.get_bb())
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom

        if self.name == MAP_one_Enemy[0]:
            if not self.invers:
                self.image.clip_draw(40 * int(self.frame),1190 - 24 , 24, 24,sx, sy, self.width, self.height)
                self.image.clip_composite_draw(int(self.frame) * 40, 1190 - 24, 24, 24,
                                               0, '', sx, sy, self.width, self.height)
            else :
                self.image.clip_composite_draw(int(self.frame) * 40, 1190 - 24, 24, 24,
                                               0, 'h', sx, sy, self.width, self.height)
                pass
            pass
        elif self.name == MAP_one_Enemy[1]:
            if not self.invers:
                self.image.clip_draw(40 *  int(self.frame),1190 - 58 - 24 , 24, 24,sx, sy, self.width, self.height)
            else :
                self.image.clip_draw(40 *  int(self.frame),1190 - 90 - 24, 24, 24,sx, sy, self.width, self.height)
                pass
        elif self.name == MAP_one_Enemy[2]:
            if not self.invers:
                self.image.clip_draw(40 *  int(self.frame),1190 - 128 - 29, 33, 29,sx, sy, self.width, self.height)
            else :
                self.image.clip_draw(40 *  int(self.frame),1190 - 162 - 29, 33, 29,sx, sy, self.width, self.height)

        elif self.name == MAP_one_Enemy[3]:
            if not self.invers:
                self.image.clip_composite_draw(int(self.frame) * 40, 1190 - 202 - 29, 28, 28,
                                               0, '', sx, sy, self.width, self.height)
            else :
                self.image.clip_composite_draw(int(self.frame) * 40, 1190 - 202 - 29, 28, 28,
                                               0, 'h', sx, sy, self.width, self.height)

        elif self.name == MAP_one_Enemy[4]:
            if not self.invers:
                self.image.clip_composite_draw(int(self.frame) * 50, 1190 - 282 - 35, 50, 35,
                                               0, '', sx, sy, self.width, self.height)
            else :
                self.image.clip_composite_draw(int(self.frame) * 50, 1190 - 282 - 35, 50, 35,
                                               0, 'h', sx, sy, self.width, self.height)

        elif self.name == MAP_one_Enemy[5]:
            if not self.invers:
                self.image.clip_composite_draw(int(self.frame) * 40, 1190 - 202 - 29, 28, 28,
                                               0, '', sx, sy, self.width, self.height)
            else :
                self.image.clip_composite_draw(int(self.frame) * 40, 1190 - 202 - 29, 28, 28,
                                               0, '', sx, sy, self.width, self.height)

        self.Hpimage.clip_draw(280, 512-158 -9, 9,9, sx, sy + 10, 30,4)
        self.Hpimage.clip_draw(422, 512-158 -9, 9,9,sx, sy + 10, self.Hp/self.MaxHp * 30,4)
        pass

    def get_bb(self):
        return self.sx - self.width//2, self.sy - self.height//2, self.sx + self.width//2, self.sy + self.height//2

    def update(self,player_x, player_y):
        global clear
        self.sx, self.sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        if self.x > player_x:
            self.invers = True
        else:
            self.invers = False

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) %6
        if self.Hp <= 0:
            if self.name == MAP_one_Enemy[5]:
                play_state.game_clear = True
            game_world.remove_object(self)
            server.ui_Manager.kill_Enemy += 1

        direction = math.atan2(player_y - self.y, player_x - self.x)
        self.x += math.cos(direction) * RUN_SPEED_PPS * game_framework.frame_time * self.speed
        self.y += math.sin(direction) * RUN_SPEED_PPS * game_framework.frame_time * self.speed
        pass

    def handle_collision(self, other, group):
        pass

    @staticmethod
    def spawnEnemy(Timer, Enemys):
        global createBoss
        newEnemy = Enemy(MAP_one_Enemy[0])
        game_world.add_object(newEnemy, 1)
        Enemys.append(newEnemy)
        if Timer > 10.0 and Timer < 40.0:
            newEnemy = Enemy(MAP_one_Enemy[1])
            game_world.add_object(newEnemy, 1)
            Enemys.append(newEnemy)

        if Timer > 30.0 and Timer < 60.0:
            newEnemy = Enemy(MAP_one_Enemy[2])
            game_world.add_object(newEnemy, 1)
            Enemys.append(newEnemy)

        if Timer > 40.0 and Timer < 80.0:
            newEnemy = Enemy(MAP_one_Enemy[3])
            game_world.add_object(newEnemy, 1)
            Enemys.append(newEnemy)
        if Timer > 60.0:
            newEnemy = Enemy(MAP_one_Enemy[4])
            game_world.add_object(newEnemy, 1)
            Enemys.append(newEnemy)

        if not play_state.createBoss and Timer > 0:
            play_state.createBoss = True
            newEnemy = Enemy(MAP_one_Enemy[5])
            game_world.add_object(newEnemy, 1)
            Enemys.append(newEnemy)

        del newEnemy

        pass


