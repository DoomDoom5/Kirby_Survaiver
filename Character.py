from pico2d import *

# 캐릭터가 가져야 할것
class Player:
    image = None
    frame = 0
    state = "IDLE"
    x = 1280//2
    y = 720//2

    x_dir = 0
    y_dir = 0

    speed = 1.2  # 이동속도

    MaxHp = 100.0  # 최대 Hp
    Hp = MaxHp  # 현재 HP

    MaxExp = 5
    Exp = 0

    Level = 0
    Power = 0.0  # 공격력
    Defence = 0.0  # 방어력
    Recovery = 0.0  # 재생력

    BulletSpeed = 1.0  # 투사채 속도
    BulletRange = 1.0  # 투사채 크기
    BulletNum = 1  # 추가 투사체 수

    Luck = 0.0  # 운에 따라 선택지 4개
    Magent = 0.0  # 경험치 흡수 범위
    Revival = 0  # 부활 횟수

    invisivleTime = 0.0  # 최대 무적시간
    Max_invisivleTime = 0.0  # 총 무적시간

    invers = False # 캐릭터 오른쪽, 왼쪽

    def draw(self):
        if self.invers != True:
            if self.state == "IDLE":
                self.frame = self.frame % 2 + 1
                if not self.invers:
                    self.image.clip_draw(0 + self.frame * 34, 616 - 80, 34, 33, self.x, self.y)
                else :
                    self.image.clip_draw(34 * self.frame - self.frame * 34, 616 - 80, 34, 33, self.x, self.y)

            elif self.state == "RUN":
                self.frame = self.frame % 7 + 1
                self.image.clip_draw(112 + self.frame * 34, 616 - 80, 34, 33, self.x, self.y)
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == SDL_KEYDOWN:
                print(self.x_dir, self.y_dir)
                self.state = "RUN"
                if event.key == SDLK_RIGHT:
                    self.x_dir += 1
                    inverse = False
                elif event.key == SDLK_LEFT:
                    self.x_dir -= 1
                    self.inverse = True
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

class Enemy:
    name = None
    image = None
    frame = 0
    state = None

    x = 0
    y = 0

    x_dir = 0
    y_dir = 0

    speed = 1.0  # 이동속도

    MaxHp = 10.0  # 최대 Hp
    Hp = MaxHp  # 현재 HP
    Power = 0.0  # 공격력

    # BulletSpeed = 1.0  # 투사채 속도
    # BulletRange = 1.0  # 투사채 크기
    # BulletNum = 1  # 추가 투사체 수

    invers = False # 캐릭터 오른쪽, 왼쪽

    def draw(self):
        if self.invers != True:
            if self.state == "IDLE":
                self.frame = self.frame % 2 + 1
                if not self.invers:
                    self.image.clip_draw(0 + self.frame * 34, 616 - 80, 34, 33, self.x, self.y)
                else :
                    self.image.clip_draw(34 * self.frame - self.frame * 34, 616 - 80, 34, 33, self.x, self.y)

            elif self.state == "RUN":
                self.frame = self.frame % 7 + 1
                self.image.clip_draw(112 + self.frame * 34, 616 - 80, 34, 33, self.x, self.y)
        pass

    def chase(self, player):
        if self.x > player.x:
            self.x_dir = -1
        else :
            self.x_dir = +1

        if self.y > player.y:
            self.y_dir = -1
        else:
            self.y_dir = 1

        pass
    def Move(self, MapEndLeft = 0, MapEndRight = 1280, MapEndBottom = 720, MapEndTop = 0):
        if self.x > MapEndLeft and self.x < MapEndRight :
            self.x += self.x_dir * self.speed

        if self.y < MapEndBottom and self.y > MapEndTop :
            self.y += self.y_dir * self.speed
        pass