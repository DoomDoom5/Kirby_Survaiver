import GameObject
from pico2d import *

# 캐릭터가 가져야 할것
class Player:
    def __init__(self):
        self.image = load_image('sprite/Kirby/Ice_Kirby_empty.png')
        self.frame = 0
        self.state = "IDLE"

        self.x = 0
        self.y = 0

        self.speed = 0.0 # 이동속도
        self.Hp = 0.0 # 현재 HP
        self.MaxHp = 0.0 # 최대 Hp
        self.Power = 0.0 # 공격력
        self.Defence = 0.0 # 방어력
        self.Recovery = 0.0 # 재생력

        self.BulletSpeed = 1.0 # 투사채 속도
        self.BulletRange = 1.0 # 투사채 크기
        self.BulletNum = 1 # 추가 투사체 수

        self.Luck = 0.0 # 운에 따라 선택지 4개
        self.Magent = 0.0 # 경험치 흡수 범위
        self.Revival = 0 # 부활 횟수


        self.invisivleTime = 0.0 # 최대 무적시간
        self.Max_invisivleTime = 0.0 # 총 무적시간

        def CollsionCheck(enemy):
            pass

        self.invers = False # 캐릭터 오른쪽, 왼쪽
        def Player_handle_events(key):
            events = get_events()
            for event in events:
                if event.type == SDL_QUIT:
                    running = False
                elif event.type == SDL_KEYDOWN:
                    self.state = "RUN"
                    if event.key == SDLK_RIGHT:
                        self.speed += 1
                        inverse = False
                    elif event.key == SDLK_LEFT:
                        self.speed -= 1
                        self.inverse = True
                    elif event.key == SDLK_UP:
                        self.speed += 1
                    elif event.key == SDLK_DOWN:
                        self.speed -= 1

                    elif event.key == SDLK_ESCAPE:
                        running = False

                elif event.type == SDL_KEYUP:
                    if event.key == SDLK_RIGHT:
                        self.speed -= 1
                    elif event.key == SDLK_LEFT:
                        self.speed += 1
                    elif event.key == SDLK_UP:
                        self.speed -= 1
                    elif event.key == SDLK_DOWN:
                        self.speed += 1
                    else :
                        self.state = "IDLE"
            pass

        def MapScollCheck(speed):
            pass

        def Animaition(state, inverse, frame):
            if inverse != True:
                if state == "IDLE":
                    pass
                elif state == "RUN":
                    frame = frame % 8
                    self.clip_draw(112 + frame * 34, 616 - 80, 34, 33, self.x, self.y)
                    pass

            else:
                if state == "IDLE":
                    pass
                elif state == "RUN":
                    pass

            pass


        def PlayerMove(MapEndLeft, MapEndRight ,MapEndTop, MapEndBottom):
            if self.x < MapEndLeft and self.x > MapEndRight:
                self.x += self.x_dir * 5
            elif self.x >= MapEndLeft :
                x = MapEndLeft
            elif self.x <= MapEndRight:
                x = 55

            if (self.y < MapEndBottom and self.y > MapEndTop):
                self.y += self.speed * 5
            elif self.y >= MapEndBottom:
                self.y = MapEndBottom
            elif self.y <= MapEndTop:
                self.y = 55

            pass


