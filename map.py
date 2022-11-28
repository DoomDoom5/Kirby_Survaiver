from pico2d import *

Maps = ['assets/img/tilesets/Map1.jpg', 'assets/img/tilesets/Map2.jpg']
class Map:
    image = None
    x = None
    y = None
    dx = None
    dy = None
    def __init__(self, MapType):
        self.image = load_image(Maps[MapType])
        self.x = self.image.w
        self.y = self.image.h



    def draw(self):
       # self.image.clip_draw(self.dx - 1280//2,self.dy - 720//2, self.x + 1280//2, self.y + 720//2, 1280 // 2, 720 // 2,1280,720)
       self.image.clip_draw(0, 0, self.x, self.y, 1280 // 2, 720 // 2, 1280, 720)
       # if dx > 1280//2 and dx < self.x - 1280//2 and dy > 720//2 and dy < self.x - 720//2:

    def update(self, player_x = 1500, player_y = 1000):
        self.dx = int(player_x)
        self.dy = int(player_y)

