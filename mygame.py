import pico2d
import game_framework

from game_states import logo_state

pico2d.open_canvas(1280,720)
game_framework.run(logo_state)
pico2d.clear_canvas()

# fill here