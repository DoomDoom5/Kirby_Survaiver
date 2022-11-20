import random
from pico2d import *
import game_world

class Enemy:
    frame = 0
    state = None
    name = None
    image = None
    Hpimage = None
    x = 0
    y = 0
    width = 0
    height = 0

    x_dir = 0
    y_dir = 0

    speed = 0  # 이동속도
    MaxHp = 10.0  # 최대 Hp
    Hp = MaxHp
    power = 0  # 공격력
    invers = False # 캐릭터 오른쪽, 왼쪽
    crystal = None

    def __init__(self):
        if Enemy.image == None:
            Enemy.image = load_image("assets/img/Enemy/Normal_Enemy.png")
            pass
        if Enemy.Hpimage == None:
            Enemy.Hpimage = load_image("assets/Ui/UI.png")
            pass

        randp = random.randint(0,4)

        if randp == 0:
            self.x = random.randint(-10,0)
            self.y = random.randint(0,720)
        elif randp == 1:
            self.x = random.randint(1280,1290)
            self.y = random.randint(0,720)
        elif randp == 2:
            self.x = random.randint(0,1280)
            self.y = random.randint(-10,0)
        else:
            self.x = random.randint(0,1280)
            self.y = random.randint(720,730)




        if self.name == "Waddle_dee":
            self.MaxHp = 10
            self.speed = 0.5
            self.width = 26
            self.height = 26
            self.power = 2
            self.crystal = "GREEN"


        elif self.name == "kinght":
            self.MaxHp = 20
            self.speed = 1
            self.width = 30
            self.height = 30
            self.power = 4
            self.crystal = "BLUE"

        elif self.name == "Fighter":
            self.MaxHp = 40
            self.speed = 3
            self.width = 35
            self.height = 35
            self.power = 6
            self.crystal = "RED"

        elif self.name == "Mike":
            self.MaxHp = 100
            self.speed = 1
            self.width = 40
            self.height = 40
            self.power = 10
            self.crystal = "RED"

        elif self.name == "NinjaCat":
            self.MaxHp = 80
            self.speed = 3
            self.width = 33
            self.height = 30
            self.power = 8
            self.crystal = "RED"

        elif self.name == "KingDedede":
            self.MaxHp = 500
            self.speed = 4
            self.width = 100
            self.height = 100
            self.power = 20
            self.crystal = "GOLD"

        self.Hp = self.MaxHp

    def On_damege(self, charater_Attack):
        self.Hp = self.Hp - charater_Attack

    def draw(self):
        self.frame = self.frame%4 + 1
        self.Hpimage.clip_draw(280, 512-158 -9, 9,9, self.x, self.y + 10, 30,4)
        self.Hpimage.clip_draw(422, 512-158 -9, 9,9, self.x, self.y + 10, self.Hp/self.MaxHp * 30,4)
        if self.name == "Waddle_dee":
            if not self.invers:
                self.image.clip_draw(40 * self.frame,1190 - 24 , 24, 24,self.x,self.y, self.width, self.height)
            else :
                self.image.clip_draw(40 * self.frame,1190 - 50 , 24, 24,self.x,self.y, self.width, self.height)
                pass
            pass
        elif self.name == "kinght":
            if not self.invers:
                self.image.clip_draw(40 * self.frame,1190 - 58 - 24 , 24, 24,self.x,self.y, self.width, self.height)
            else :
                self.image.clip_draw(40 * self.frame,1190 - 90 - 24, 24, 24,self.x,self.y, self.width, self.height)
                pass
        elif self.name == "Fighter":
            if not self.invers:
                self.image.clip_draw(40 * self.frame,1190 - 128 - 29, 33, 29,self.x,self.y, self.width, self.height)
            else :
                self.image.clip_draw(40 * self.frame,1190 - 162 - 29, 33, 29,self.x,self.y, self.width, self.height)

        pass

    def chase(self, player_x, player_y):
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

    def get_bb(self):
        return self.x - self.width//2, self.y - self.height//2, self.x + self.width//2, self.y + self.height//2

    def update(self,player_x, player_y):
        dgree = 0
        if self.Hp <= 0:
            game_world.remove_object(self)
        self.chase(player_x, player_y)
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

        self.x += math.cos(math.radians(dgree)) * self.speed
        self.y += math.sin(math.radians(dgree)) * self.speed
        pass