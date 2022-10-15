from pico2d import *
import game_framework
from Character import Player
from Character import Enemy

class rect:
    left = 0
    right = 0
    bottom = 0
    top = 0
    pass

max_col = 40
max_row = 40

kirby = Player()

Enemys = [Enemy in range(0,10)]

# tiles = [[rect for j in range(max_col)] for i in range(max_row)]
BG_tile_image = None
def enter():
    global BG_tile_image, tiles, kirby
    BG_tile_image = load_image("assets/img/tilesets/ForestTexturePacked.png")
    kirby.image = load_image("assets/img/Kirby/Ice_Kirby_empty.png")


def exit():
    global BG_tile_image
    del BG_tile_image
    pass

def update():
    kirby.Move()
    pass

def draw():
    clear_canvas()
    for col in range(0, max_col):
        for row in range(0, max_row):
            BG_tile_image.clip_draw(205,206,102,102,102 * col, 102 * row)
        pass
    kirby.draw()
    update_canvas()
    # fill here
    pass

def handle_events():
    events = get_events()
    kirby.handle_events(events)
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()






