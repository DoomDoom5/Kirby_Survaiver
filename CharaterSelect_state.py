from pico2d import *
import game_framework
import title_state

# fill here
image = None

def enter():
    global image
    image = load_image("assets/title/tuk_credit.png")
    # fill here
    pass

def exit():
    global image
    del image
    # fill here
    pass

def update():

    # fill here
    pass

def draw():
    clear_canvas()
    image.draw(1280//2,720//2)
    update_canvas()
    # fill here
    pass

def handle_events():
    events = get_events()





