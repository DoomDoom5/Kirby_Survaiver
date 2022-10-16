from pico2d import *

class Item_Manager:
    Weapons = 0
    weaponsImage = None
    Accessories = 0
    AccessoriesImage = None
    pass


class Weapon:

    x = 0
    x_dir = 0
    y = 0
    y_dir = 0

    Name = None
    Attack = 0 # 공격력
    level = 0 # 레벨
    responTime = 0

    BulletSpeed = 1.0  # 투사채 속도
    BulletRange = 1.0  # 투사채 크기
    BulletNum = 1  # 추가 투사체 수
    pass

class Ice(Weapon): # 가까운적 찾고 그냥 일직선 공격
    def __init__(self):
        self.Attack = 3

    def move(self):
        pass


    def draw(self,image):
        image.clip_draw(0,0,50,50,100,100,self.x,self.y)
        pass
class Hammer(Weapon): # 해머 공격 == 뱀서의 도끼 공격

    pass
