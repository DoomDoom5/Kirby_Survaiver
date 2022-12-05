from pico2d import *

Maps = ['assets/img/tilesets/Map1.jpg', 'assets/img/tilesets/Map2.jpg']
Bgms = ['assets/sounds/bgm_forest.ogg', 'assets/sounds/bgm_library.ogg']
class Map:
    image = None
    bgm = None
    x = None
    y = None
    dx = None
    dy = None
    def __init__(self, MapType):
        self.image = load_image(Maps[MapType])
        self.bgm = load_music(Bgms[MapType])
        self.bgm.repeat_play()
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h



    def draw(self):
        self.image.clip_draw_to_origin(
            self.window_left, self.window_bottom,
            self.canvas_width, self.canvas_height,
            0, 0)

    def update(self, player_x = 1500, player_y = 1000):

        self.window_left = clamp(0, int(player_x) - self.canvas_width//2,
                                 self.w - self.canvas_width - 1)
        # 0 ~ x ~ 배경의 오른쪽 - 윈도우창 - 1
        self.window_bottom = clamp(0, int(player_y) - self.canvas_height//2,
                                 self.h - self.canvas_height - 1)
        # 0 ~ y ~ 배경의 위쪽 - 윈도우창 - 1

