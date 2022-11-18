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

    def __init__(self):
        if Enemy.image == None:
            Enemy.image = load_image("assets/img/Enemy/Normal_Enemy.png")
            pass
        if Enemy.Hpimage == None:
            Enemy.Hpimage = load_image("assets/Ui/UI.png")
            pass

        self.x = random.randint(-10,0)
        self.y = random.randint(0,720)
        if self.name == "Waddle_dee":
            self.MaxHp = 10
            self.speed = 0.5
            self.width = 24
            self.height = 24
            self.power = 2

        elif self.name == "kinght":
            self.MaxHp = 20
            self.speed = 1
            self.width = 24
            self.height = 24
            self.power = 4

        elif self.name == "Fighter":
            self.MaxHp = 40
            self.speed = 3
            self.width = 24
            self.height = 24
            self.power = 7

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
                self.image.clip_draw(40 * self.frame,1190 - 100 - 24 , 24, 24,self.x,self.y, self.width, self.height)
            else :
                self.image.clip_draw(40 * self.frame,1190 - 130 - 24, 24, 24,self.x,self.y, self.width, self.height)

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
    def Move(self):
        self.x += self.x_dir * self.speed
        self.y += self.y_dir * self.speed


    def update(self):
        if self.Hp <= 0:
            game_world.remove_object(self)
        pass