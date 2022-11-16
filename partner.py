from pico2d import *


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


