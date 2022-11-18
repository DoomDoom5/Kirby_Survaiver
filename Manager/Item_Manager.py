import random
import game_world
from pico2d import *


class Item:
    Name = None
    Gained = None
    x = 0
    y = 0
class ExpStone(Item):
    Type = None
    Exp = None
    Magnet = None
    def __init__(self,Enemy_x=0, Enemy_y=0):
        self.width = 12
        self.height = 18
        self.Magnet = False
        self.Gained = False
        self.x = Enemy_x
        self.y = Enemy_y
        self.Name = "EXP_STONE"
        self.t = 0.0
        match self.Type:
            case "GREEN":
                self.Exp = 2
            case "BLUE":
                self.Exp = 5
            case "RED":
                self.Exp = 10
            case "YEELOW":
                self.Exp = 20

    def Magnet_Player(self, Player_x=0, Player_y=0, Player_Magnet_Range=0):
        if self.Magnet:
            self.t += 0.01
            self.x = (1-self.t) * self.x+ self.t * Player_x
            self.y = (1-self.t) * self.y+ self.t * Player_y
            if self.x - self.width//2 < Player_x - 5 \
                    and self.y - self.height//2 < Player_y - 5 \
                    and self.x + self.width//2 > Player_x + 5 \
                    and self.y + self.height//2 > Player_y + 5:
                self.Gained = True
            
        else:
            if self.x  > Player_x - Player_Magnet_Range \
                    and self.y > Player_y - Player_Magnet_Range \
                    and self.x < Player_x + Player_Magnet_Range \
                    and self.y < Player_y + Player_Magnet_Range : # 마그넷 충돌 검사
                self.Magnet = True


    def Draw(self, Item_Image):
        match self.Type:
            case "GREEN":
                Item_Image.clip_draw(51, 624 - 96 - 12, 9,12,self.x,self.y,self.width, self.height)
            case "BLUE":
                Item_Image.clip_draw(51, 624 - 36 - 12, 9, 12, self.x, self.y,self.width, self.height)
            case "RED":
                Item_Image.clip_draw(51, 624 - 526 - 12, 9, 12, self.x, self.y,self.width, self.height)
        pass

class Item_manager:
    Items = []
    Items_image = None
    expStone = ExpStone()
    def __init__(self):
        if Item_manager.Items_image == None:
            Item_manager.Items_image = load_image("assets/Ui/items.png")

    def Create_EXP_Stone(self, Enemy_crystal, Enemy_x, Enemy_y):
        newExpStone = ExpStone()
        newExpStone.Type = Enemy_crystal
        newExpStone.__init__(Enemy_x,Enemy_y)
        self.Items.append(newExpStone)
        del newExpStone

    def draw(self):
        for item in self.Items:
            match item.Name:
                case "EXP_STONE":
                    self.expStone = item
                    self.expStone.Draw(self.Items_image)

    def update(self):
        pass

    def GainExp(self, Player_x, Player_y, Player_Magnet_Range, Player_Exp):
        for item in self.Items:
            if item.Gained:
                self.Items.remove(item)
            else:
                match item.Name :
                    case "EXP_STONE":
                        self.expStone = item
                        self.expStone.Magnet_Player(Player_x, Player_y, Player_Magnet_Range)
                        if item.Gained:
                            Player_Exp = self.expStone.Exp
                            self.Items.remove(item)
                            return Player_Exp

        return 0


class Missile:
    # ICE, FIRE, HAMMER 등등등
    name = "None"
    # state = 0 : 발사중, 1 : 파괴, 2 : 소멸
    state = None
    image = None
    x = 0
    y = 0
    x_dir = 0

    level = 1 # 레벨

    width = 0 # 너비
    height = 0 # 크기

    Attack = 0 # 공격력
    BulletSpeed = 1.0  # 투사채 속도
    BulletRange = 1.0  # 투사채 크기
    BulletNum = 1  # 추가 투사체 수

    DurationTime = 0
    ice = None
    Fire = None


class ICE(Missile): # 가로로 일직선 공격
    def __init__(self, level=0, invers=False,charater_x = 0,charater_y = 0,charater_Attack = 0):
        self.frame = 0
        self.state = 0
        self.width = 24
        self.height = 24
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

        if level == 1:
            self.DurationTime = 4.0
            pass
        elif level == 2:
            pass
        elif level == 3:
            pass
    def Move(self, MapEndLeft=0, MapEndRight=1280, MapEndBottom=720, MapEndTop=0):
        if self.state == 0:
            self.x += self.x_dir * self.BulletSpeed
            if self.x > MapEndRight:
                del self
            elif self.x < MapEndLeft:
                del self
        elif self.state == 1:
            if self.state >= 8:
                self.state = 2

    def draw(self, image):
        if self.state == 0:
            image.clip_draw(365, 552-45 - 24, 24,24,self.x,self.y, self.width * self.BulletRange, self.height * self.BulletRange)
        elif self.state == 1:
            self.frame = self.frame+1
            match self.frame//2:
                case 0 :
                    image.clip_draw(245, 552-19 - 10, 20,20,self.x,self.y,self.width * 2 * self.BulletRange,self.height * 2 * self.BulletRange)
                case 1 :
                   image.clip_draw(265, 552-19 - 10, 20,20,self.x,self.y,self.width * 2 * self.BulletRange,self.height * 2 * self.BulletRange)
                case 2 :
                   image.clip_draw(291, 552-19 - 10, 30,30,self.x,self.y,self.width  * 2* self.BulletRange,self.height * 2 * self.BulletRange)
                case 3 :
                    image.clip_draw(335, 552-19 - 10, 30,30,self.x,self.y,self.width * 2 * self.BulletRange,self.height * 2 * self.BulletRange)
                case 4 :
                   image.clip_draw(373, 552-19 - 10, 30,30,self.x,self.y,self.width * 2 * self.BulletRange,self.height * 2 * self.BulletRange)
        pass
class FIRE(Missile): # 무작위 위치에 불덩이 낙하
    def __init__(self, level=0, invers=False):
        self.frame = 0
        self.state = 0

        self.x = random.randint(0,200)


        self.width = 24
        self.height = 24
        self.BulletRange = 1.0
        self.BulletSpeed = 5.0  # 투사채 속도
        self.Attack = 20

        if level == 1:
            self.DurationTime = 4.0
            pass
        elif level == 2:
            pass
        elif level == 3:
            pass
    def Move(self, MapEndLeft=0, MapEndRight=1280, MapEndBottom=720, MapEndTop=0):
        if self.state == 0:
            self.y += self.y_dir * self.BulletSpeed
            if self.y > MapEndRight:
                del self
            elif self.y < MapEndLeft:
                del self
        elif self.state == 1:
            if self.state >= 8:
                self.state = 2

    def draw(self, Image):

        pass
class PLASMA(Missile): # 가까운적 찾고 그냥 가로로 일직선 공격
    A = 4
    def __init__(self, level=0, invers=False):
        self.frame = 0
        self.state = 0
        self.width = 24
        self.height = 24
        self.BulletRange = 1.0
        self.BulletSpeed = 5.0  # 투사채 속도
        if invers:
            self.x_dir = 1
        else:
            self.x_dir = -1
            pass

        if level == 1:
            self.DurationTime = 4.0
            pass
        elif level == 2:
            pass
        elif level == 3:
            pass
    def Move(self, MapEndLeft=0, MapEndRight=1280, MapEndBottom=720, MapEndTop=0):
        if self.state == 0:
            self.x += self.x_dir * self.BulletSpeed
            if self.x > MapEndRight:
                del self
            elif self.x < MapEndLeft:
                del self
        elif self.state == 1:
            if self.state >= 8:
                self.state = 2

    def draw(self, Image):
        if self.state == 0:
            Image.clip_draw(365, 552-45 - 24, 24,24,self.x,self.y, self.width * self.BulletRange, self.height * self.BulletRange)
        elif self.state == 1:
            self.frame = self.frame+1
            match self.frame//2:
                case 0 :
                    Image.clip_draw(245, 552-19 - 10, 20,20,self.x,self.y,self.width * 2 * self.BulletRange,self.height * 2 * self.BulletRange)
                case 1 :
                    Image.clip_draw(265, 552-19 - 10, 20,20,self.x,self.y,self.width * 2 * self.BulletRange,self.height * 2 * self.BulletRange)
                case 2 :
                    Image.clip_draw(291, 552-19 - 10, 30,30,self.x,self.y,self.width  * 2* self.BulletRange,self.height * 2 * self.BulletRange)
                case 3 :
                    Image.clip_draw(335, 552-19 - 10, 30,30,self.x,self.y,self.width * 2 * self.BulletRange,self.height * 2 * self.BulletRange)
                case 4 :
                    Image.clip_draw(373, 552-19 - 10, 30,30,self.x,self.y,self.width * 2 * self.BulletRange,self.height * 2 * self.BulletRange)
        pass

class HAMMER(Missile): # 해머 공격 == 뱀서의 도끼 공격
    UpTime = None
    def __init__(self, level=0, invers=False, charater_x=0, charater_y=0):
        self.x = charater_x
        self.y = charater_y
        self.width = 24
        self.height = 24
        self.BulletRange = 1.0
        self.BulletSpeed = 5.0  # 투사채 속도
        self.Attack = 13
        self.UpTime = 5.0
        if invers:
            self.x_dir = 1
        else:
            self.x_dir = -1
            pass

        if level == 1:
            self.DurationTime = 4.0
            pass
        elif level == 2:
            pass
        elif level == 3:
            pass

    def Move(self, MapEndLeft=0, MapEndRight=1280, MapEndBottom=720, MapEndTop=0):
        if self.UpTime:
            pass

        self.x += self.x_dir
        if self.x > MapEndRight:
            del self
        elif self.x < MapEndLeft:
            del self
        pass


class Missile_manager:
    missiles = []
    ice = ICE()
    fire = FIRE()
    plasma = PLASMA()
    hammer = HAMMER()
    image = None

    def __init__(self):
        if Missile_manager.image == None:
            Missile_manager.image = load_image("assets/img/Effect/vfx.png")

    def draw(self):
        for missile in self.missiles:
            if missile.name == "ICE":
                self.ice = missile
                self.ice.draw(self.image)
            elif missile.name == "HAMMER":
                self.hammer.draw(self.image)
                pass

    def update(self):
        for missile in self.missiles:
            if missile.state == 2:
                self.missiles.remove(missile)
                game_world.remove_object(self)
            elif missile.name == "ICE":
                self.ice = missile
                self.ice.Move()
            elif missile.name == "HAMMER":
                self.hammer.Move()
                pass
        pass

    def get_bb(self):
        for missile in self.missiles:
            if missile.state == 0:
                return missile.x - missile.width // 2, missile.y - missile.height // 2, missile.x + missile.width // 2, missile.y + missile.height // 2
    def Check_Hit_Enemy(self, enemy_left , enemy_right , enemy_top , enemy_bottom):
         for missile in self.missiles:
             if missile.state == 0:
                 if missile.x - missile.width < enemy_right and missile.y - missile.height < enemy_bottom and missile.x + missile.width > enemy_left and missile.y + missile.height > enemy_top:
                     missile.x = (enemy_left + enemy_right)//2
                     missile.state = 1
                     return missile.Attack
         return 0


class Weapon:
    name= "None"
    shotTimer = 0.0
    coolTime = 1.0

    level = 1

    def shot(self, charater_x, charater_y,charater_Attack  ,charater_invers, missile_manager, Timer = 0.03):
        if self.shotTimer >= self.coolTime:
            if self.name == "ICE":
                new_missile = ICE()
                new_missile.name = self.name
                new_missile.__init__(self.level,charater_invers,charater_x,charater_y,charater_Attack)
                missile_manager.missiles.append(new_missile)
                del new_missile
            elif self.name == "HAMMER":
                pass
            self.shotTimer = 0.0

        else:
            self.shotTimer = self.shotTimer + Timer

    pass


