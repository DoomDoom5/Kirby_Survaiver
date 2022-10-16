from pico2d import *
import Manager.Item_Manager

# 캐릭터가 가져야 할것
class Player:
    image = None
    effect_Image = None
    type = None
    frame = 0
    state = "IDLE"

    x = 1280//2
    y = 720//2
    width = 40
    height = 40

    x_dir = 0
    y_dir = 0

    speed = 2  # 이동속도

    MaxHp = 100.0  # 최대 Hp
    Hp = MaxHp  # 현재 HP

    MaxExp = 5
    Exp = 0

    Level = 0

    Defence = 0.0  # 방어력
    Recovery = 0.0  # 재생력

    BulletSpeed = 1.0  # 투사채 속도
    BulletRange = 1.0  # 투사채 크기
    BulletNum = 1  # 추가 투사체 수

    Luck = 0.0  # 운에 따라 선택지 4개
    Magent = 0.0  # 경험치 흡수 범위
    Revival = 0  # 부활 횟수

    invisivleTime = 0.0  # 무적시간
    Max_invisivleTime = 1.0  # 최대 무적시간
    invers = False # 캐릭터 오른쪽, 왼쪽

    def __init__(self):
            pass

    def check_Enemy_Coll(self, enemy_left, enemy_right, enemy_top, enemy_bottom, enemy_Attack):
        if self.x - self.width//2 < enemy_right and self.y - self.height//2 < enemy_bottom and self.x + self.width//2 > enemy_left and self.y + self.height//2 > enemy_top:
            if self.invisivleTime <= 0:
                self.Hp -= enemy_Attack
                self.invisivleTime = self.Max_invisivleTime
        pass
    def draw(self):
        self.frame = self.frame+1
        if self.invisivleTime > 0 and self.frame%2 == 0:
            pass
        else:
            if self.state == "IDLE":
                self.frame = self.frame % 2
                if not self.invers:
                    self.image.clip_draw(0 + self.frame * 34, 616 - 80, 34, 33, self.x, self.y, self.width,self.height)
                else :
                    self.image.clip_draw(0 + self.frame * 34, 616 - 40, 34, 33, self.x, self.y, self.width,self.height)

            elif self.state == "RUN":
                self.frame = self.frame % 6
                if not self.invers:
                    self.image.clip_draw(114 + self.frame * 33, 616 - 80, 33, 33, self.x, self.y, self.width,self.height)
                else:
                    self.image.clip_draw(114 + self.frame * 34, 616 - 40, 34, 33, self.x, self.y, self.width,self.height)
        pass
    def handle_events(self, events):
        for event in events:
            if event.type == SDL_KEYDOWN:
                self.state = "RUN"
                if event.key == SDLK_RIGHT:
                    self.x_dir += 1
                    self.invers = True
                elif event.key == SDLK_LEFT:
                    self.x_dir -= 1
                    self.invers = False
                elif event.key == SDLK_UP:
                    self.y_dir += 1
                elif event.key == SDLK_DOWN:
                    self.y_dir -= 1

            elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    self.x_dir -= 1
                elif event.key == SDLK_LEFT:
                    self.x_dir += 1
                elif event.key == SDLK_UP:
                    self.y_dir -= 1
                elif event.key == SDLK_DOWN:
                    self.y_dir += 1

            if self.x_dir == 0 and self.y_dir == 0:
                self.state = "IDLE"
            pass

    def Attack_Weapons(self):
        for Weapon in self.Weapons:
            Weapon.Attack()
            pass


    def ExpMagnet(self):
        pass
    def levelUP(self):
        if self.Exp >= self.MaxExp:
            self.Exp = 0
            self.MaxExp = self.MaxHp * 1.5
            self.Level = self.Level + 1
        pass
    def Move(self, MapEndLeft = 0, MapEndRight = 1280, MapEndBottom = 720, MapEndTop = 0):
        if self.x > MapEndLeft and self.x < MapEndRight:
            self.x += self.x_dir * self.speed
        elif self.x < MapEndRight - 20:
            self.x = 20
        elif self.x > MapEndLeft + 20:
            self.x = 1260


        if self.y < MapEndBottom and self.y > MapEndTop:
            self.y += self.y_dir * self.speed
        elif self.y < MapEndBottom - 20:
            self.y = 20
        elif self.y > MapEndTop + 20:
            self.y = 700


        pass
class Partner:
    image = None
    type = None
    frame = 0
    state = "IDLE"

    x = 1280 // 2
    y = 720 // 2
    width = 40
    height = 40

    x_dir = 0
    y_dir = 0

    speed = 2  # 이동속도

    Power = 0.0  # 공격력
    attackCircle = 10 # 적 탐색 범위

    BulletSpeed = 1.0  # 투사채 속도
    BulletRange = 1.0  # 투사채 크기
    BulletNum = 1  # 추가 투사체 수


    invers = False  # 캐릭터 오른쪽, 왼쪽

    def draw(self):
        if self.state == "IDLE":
            self.frame = self.frame % 2 + 1
            if not self.invers:
                self.image.clip_draw(0 + self.frame * 34, 616 - 80, 34, 33, self.x, self.y, self.width, self.height)
            else:
                self.image.clip_draw(0 + self.frame * 34, 616 - 40, 34, 33, self.x, self.y, self.width, self.height)

        elif self.state == "RUN":
            self.frame = self.frame % 6 + 1
            if not self.invers:
                self.image.clip_draw(114 + self.frame * 33, 616 - 80, 33, 33, self.x, self.y, self.width, self.height)
            else:
                self.image.clip_draw(114 + self.frame * 34, 616 - 40, 34, 33, self.x, self.y, self.width, self.height)
    def Move(self, MapEndLeft=0, MapEndRight=1280, MapEndBottom=720, MapEndTop=0):
        if self.x > MapEndLeft and self.x < MapEndRight:
            self.x += self.x_dir * self.speed
        elif self.x < MapEndRight - 20:
            self.x = 20
        elif self.x > MapEndLeft + 20:
            self.x = 1260

        if self.y < MapEndBottom and self.y > MapEndTop:
            self.y += self.y_dir * self.speed
        elif self.y < MapEndBottom - 20:
            self.y = 20
        elif self.y > MapEndTop + 20:
            self.y = 700

        pass
class Enemy:
    frame = 0
    state = None
    name = None
    image = None
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
        if(self.name == "Waddle_dee"):
            self.MaxHp = 10
            self.speed = 0.5
            self.width = 24
            self.height = 24
            self.power = 2
        elif(self.name == "kinght"):

            pass

        self.Hp = self.MaxHp

    def Move(self, MapEndLeft = 0, MapEndRight = 1280, MapEndBottom = 720, MapEndTop = 0):
        self.x += self.x_dir * self.speed
        self.y += self.y_dir * self.speed

    def draw(self, image):
        self.frame = self.frame%4 + 1
        if self.name == "Waddle_dee":
            if not self.invers:
                image.clip_draw(40 * self.frame,1190 - 24 , 24, 24,self.x,self.y)
            else :
                image.clip_draw(40 * self.frame,1190 - 50 , 24, 24,self.x,self.y)
                pass
            pass
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

