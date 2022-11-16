from pico2d import *

class Map:
    image = None
    x = None
    y = None
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


    def draw(self, player_x = 1280//2, player_y = 720//2):
        dx = int(player_x)
        dy = int(player_y)

        self.image.clip_draw(dx - self.x // 2, dy - self.y // 2, 1280, 720, 1280 // 2, 720 // 2)
       # if dx > 1280//2 and dx < self.x - 1280//2 and dy > 720//2 and dy < self.x - 720//2:


