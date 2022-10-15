import pico2d
import game_framework

import logo_state
import play_state
import CharaterSelect_state

pico2d.open_canvas(1280,720)
game_framework.run(play_state)
pico2d.clear_canvas()

# fill here
