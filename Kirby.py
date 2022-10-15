from pico2d import *

class MovementObject:
    def __init__(self):
        self.hp = 100
        self.image
        self.x, self.y = 0,0
        self.state = 0
        self.frame = 0

class Kirby(MovementObject):
    def __init__(self):
        self.ablility = 0
        self.inverse = False
        self.image = load_image('sprite/Kirby/Ice_Kirby_empty.png')

    def draw_Kirby(self):
        self.frame = self.frame + 1
        self.Kirby_Walk()
        pass

    def Kirby_Walk(self, frame):
        frame = frame % 8
        self.clip_draw(114 + frame * 36, 616 - 39, 36, 33, self.x, self.y)

    def Kirby_Dash(self, frame):
        frame = frame % 8
        self.clip_draw(112 + frame * 34, 616 - 80, 34, 33, self.x, self.y)

    def Kirby_dumbring(self, frame):
        frame = frame % 11
        self.clip_draw(112 + frame * 37, 616 - 126, 37, 38, self.x, self.y)

    def Kirby_frying(self, frame):
        frame = frame % 6
        self.clip_draw(112 + frame * 40, 616 - 353, 40, 41, self.x, self.y)

    def Kirby_spin(self, frame):
        frame = frame % 8
        self.clip_draw(6 + frame * 40, 616 - 605, 40, 33, self.x, self.y)

    def Kirby_Rotate(self, frame):
        frame = frame % 8
        self.clip_draw(11 + frame * 37, 616 - 559, 37, 36, self.x, self.y)

    def Attack_Effect(self, frame):
        frame = frame % 4
        self.clip_draw(527 + frame * 72, 616 - 300, 72, 78, self.x, self.y)