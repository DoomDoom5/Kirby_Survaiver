from pico2d import *
open_canvas()

character = load_image('img/Kirby/Fire_Kirby_empty.png')

frame = 0

def Kirby_Walk (x = 0,y = 0,frame = 0):
        frame = frame%8
        character.clip_draw(114 + frame * 36, 616-39, 36, 33, x, y)

def Kirby_Dash(x = 0,y = 0,frame = 0):
        frame = frame%8
        character.clip_draw(112 + frame * 34, 616 - 80, 34, 33, x, y)

def Kirby_dumbring(x = 0,y = 0,frame = 0):
        frame = frame%11
        character.clip_draw(112 + frame * 37, 616 - 126, 37, 38, x, y)

def Kirby_frying(x = 0,y = 0,frame = 0):
        frame = frame%6
        character.clip_draw(112 + frame * 40, 616 - 353, 40, 41, x, y)

def Kirby_spin(x = 0,y = 0,frame = 0):
        frame = frame%8
        character.clip_draw(6 + frame * 40, 616 - 605, 40, 33, x, y)

def Kirby_Rotate(x = 0,y = 0,frame = 0):
        frame = frame%8
        character.clip_draw(11 + frame * 37, 616 - 559, 37, 36, x, y)

def Ice_Effect(x = 0,y = 0,frame = 0):
        frame = frame%4
        character.clip_draw(527 + frame * 72, 616 - 300, 72, 78, x, y)

# 여기를 채우세요.
while True:
        clear_canvas()

        Kirby_Walk(50,70, frame)
        Kirby_Dash(50,140, frame)
        Kirby_dumbring(50,210, frame)
        Kirby_frying(50,280, frame)
        Kirby_spin(50,350, frame)
        Kirby_Rotate(50,490, frame)
        Ice_Effect(50,420, frame)

        frame = (frame + 1) % 20
        update_canvas()
        delay(0.03)
        get_events()



close_canvas()

