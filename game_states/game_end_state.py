from pico2d import *
import game_framework
import game_world
from game_states import play_state
from game_states import logo_state
import server
Item_image = None
Type = None
box_bg_image = None
font = None
anim_height = None

game_clear = None

clear_score = None
level_score = None
kill_score = None
Timer_score = None
last_score = None

end_bgm = None
def enter():
    global box_bg_image, anim_height,game_clear, clear_score, Timer_score , level_score,kill_score,end_bgm,last_score
    anim_height = 600
    box_bg_image = load_image("assets/Ui/UI.png")
    Timer_score = 1000

    if play_state.game_clear == True:
        game_clear = "GAME CLEAR!!!"
        clear_score = 1000
        end_bgm = load_music("assets/sounds/VS_game_clear.wav")
        if server.ui_Manager.elapsed_time - 180 < 900:
            Timer_score -= (server.ui_Manager.elapsed_time - 180)
        else:
            Timer_score = 100

        print(server.ui_Manager.elapsed_time)
    else:
        game_clear = "GAME OVER...."
        end_bgm = load_music("assets/sounds/VS_GameOver_v02-01.ogg")
        clear_score = 0
        Timer_score = 0

    kill_score = server.ui_Manager.kill_Enemy * 10
    level_score = play_state.kirby.Level * 100
    last_score = level_score + kill_score + Timer_score + clear_score

    end_bgm.set_volume(server.masterVolume)
    end_bgm.play(1)
    pass


def exit():
    global box_bg_image,  clear_score, Timer_score, game_clear,last_score
    del box_bg_image,clear_score, Timer_score, game_clear,last_score
    # fill here
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            if event.x > 800 and event.x < 900 and events.y > 560 and event.y < 600:
                print(event.x, ", ", event.y)
                game_framework.quit()
                pass
        if event.type == SDL_QUIT:
            game_framework.quit()
    pass


def draw():
    clear_canvas()
    play_state.draw_world()

    box_bg_image.clip_draw(175, 512 - 131 - 48, 48, 48, 1280 // 2, anim_height + 720 // 2, 800, 720)
    server.ui_Manager.UI_font.draw(550, anim_height + 500, "Clear Point is : %d" % clear_score, (255, 255, 255))
    server.ui_Manager.UI_font.draw(550, anim_height + 400, "Level score: %d" % level_score , (255, 255, 255))
    server.ui_Manager.UI_font.draw(550, anim_height + 350, "Kill enemys score: %d" % kill_score, (255, 255, 255))
    server.ui_Manager.UI_font.draw(550, anim_height + 300, "Timer Score: %3.1f"% Timer_score ,(255, 255, 255))
    server.ui_Manager.UI_font.draw(550, anim_height + 200, "Total Score : %d"% last_score ,(255, 255, 0))

    box_bg_image.clip_draw(176, 512 - 181 - 33, 48, 33, 850, 150, 100, 60)
    server.ui_Manager.UI_font.draw(830, 720 - 570, "종료", (255, 255, 255))

    update_canvas()
    pass


def update():
    global anim_height
    if anim_height > 1:
        anim_height -= 100
    delay(0.02)
    pass


def pause():
    pass


def resume():
    pass






