from pico2d import *



class Missile:
    name = "None"
    x = 0
    y = 0
    x_dir = 0

    level = 1 # 레벨

    width = 0
    height = 0

    Attack = 0 # 공격력
    BulletSpeed = 1.0  # 투사채 속도
    BulletRange = 1.0  # 투사채 크기
    BulletNum = 1  # 추가 투사체 수

    DurationTime = 0
    def draw(self,effect_Image):
        pass

    pass

class ICE(Missile): # 가까운적 찾고 그냥 가로로 일직선 공격
    def __init__(self, level=0, invers=False, charater_x=0, charater_y=0):
        self.x = charater_x
        self.y = charater_y
        self.width = 24
        self.height = 24
        self.BulletRange = 1.0
        self.BulletSpeed = 5.0  # 투사채 속도
        if invers:
            self.x_dir = 1
        else :
            self.x_dir = -1
            pass

        if level == 1:
            self.Attack = 3
            self.DurationTime = 4.0
            pass
        elif level == 2:
            pass
        elif level == 3:
            pass
    def Move(self, MapEndLeft=0, MapEndRight=1280, MapEndBottom=720, MapEndTop=0):
        self.x += self.x_dir * self.BulletSpeed
        if self.x > MapEndRight:
            del self
        elif self.x < MapEndLeft:
            del self

    def draw(self, Image):
        Image.clip_draw(719, 616-41 - 24, 24,24,self.x,self.y, 24 * self.BulletRange, 24 * self.BulletRange)
        pass

class HAMMER(Missile): # 해머 공격 == 뱀서의 도끼 공격
    pass


class Missile_manager:
    missiles = []
    ice = ICE()
    hammer = HAMMER()
    missiles_image = None
    def draw(self):
        for missile in self.missiles:
            if missile.name == "ICE":
                self.ice = missile
                self.ice.draw(self.missiles_image)
            elif missile.name == "HAMMER":
                self.hammer.draw(self.missiles_image)
                pass

    def Move(self):
        for missile in self.missiles:
            if missile.name == "ICE":
                self.ice = missile
                self.ice.Move()
            elif missile.name == "HAMMER":
                self.hammer.Move()
                pass
        pass

    def Check_Hit_Enemy(self, enemy_left , enemy_right , enemy_top , enemy_bottom):
         for missile in self.missiles:
             if missile.x - missile.width < enemy_right and missile.y - missile.height < enemy_bottom and missile.x + missile.width > enemy_left and missile.y + missile.height > enemy_top:
                 self.missiles.remove(missile)
                 return missile.Attack
         return 0


class Weapon:
    name= "None"
    shotTimer = 0.0
    coolTime = 1.0

    level = 1

    def shot(self, charater_x, charater_y, charater_invers, missile_manager, Timer = 0.03):
        if self.shotTimer >= self.coolTime:
            if self.name == "ICE":
                new_missile = ICE()
                new_missile.name = self.name
                new_missile.__init__(self.level,charater_invers,charater_x,charater_y)
                missile_manager.missiles.append(new_missile)
            elif self.name == "HAMMER":
                pass
            self.shotTimer = 0.0

        else:
            self.shotTimer = self.shotTimer + Timer

    pass


