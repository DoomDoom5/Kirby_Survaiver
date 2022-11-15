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
        self.image.clip_draw(player_x - 1280 // 2 + 1, player_y - 720 // 2 + 1, 1280 ,720 ,1280//2, 720//2, self.x, self.y)
        # 280, 512-158 -9, 9,9, s_Enemy.x, s_Enemy.y + 10, 30,4)
        # if player_x > 1280//2 and player_x < self.x - 1280//2 and player_y > 720//2 and player_x < self.x - 720//2:
        #  self.image.clip_draw(player_x - 1280//2, player_y - 720//2, self.x, self.y, 102, 102)


