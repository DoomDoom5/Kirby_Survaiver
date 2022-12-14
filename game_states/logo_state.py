from pico2d import *
import game_framework
from game_states import title_state

# fill here
image = None
logo_time = None

def enter():
    global image, logo_time
    image = load_image("assets/title/tuk_credit.png")
    logo_time = 0.0
    pass

def exit():
    global image, logo_time
    del image, logo_time
    pass

def update():
    # logo time을 계산하고, 그 결과에 따라 1초가 넘으면 running = False
    global logo_time
    delay(0.01)
    logo_time += 0.01
    if logo_time >= 0.5:
        logo_time = 0.0
        game_framework.change_state(title_state)
    # fill here
    pass

def draw():
    clear_canvas()
    image.clip_draw(0,0,800,600,1280//2,720//2,1280,720)
    update_canvas()
    # fill here
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()





