from pico2d import *

class Map:
    image = None
    x = None
    y = None
    dx = None
    dy = None
    def __init__(self, MapName):
        if MapName == "Forest":
            self.image = load_image('assets/img/tilesets/Map1.jpg')
            self.x = 1836
            self.y = 1020
            pass

        elif MapName == "Library":
            self.image = load_image('assets/img/tilesets/Map2.jpg')
            self.x = 1938
            self.y = 816
            pass


    def draw(self):
       # self.image.clip_draw(self.dx - 1280//2,self.dy - 720//2, self.x + 1280//2, self.y + 720//2, 1280 // 2, 720 // 2,1280,720)
       self.image.clip_draw(0, 0, self.x, self.y, 1280 // 2, 720 // 2, 1280, 720)
       # if dx > 1280//2 and dx < self.x - 1280//2 and dy > 720//2 and dy < self.x - 720//2:

    def update(self, player_x = 1500, player_y = 1000):
        self.dx = int(player_x)
        self.dy = int(player_y)

