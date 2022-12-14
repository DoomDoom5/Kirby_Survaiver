from pico2d import *
import game_framework
import game_world
from game_states import play_state

class UI_Manager:
    Weapons = []
    accessories = []
    UI_Image = None
    kriby_UI_Image = None
    Item_Image = None
    UI_font = None
    Draw_x = None
    Draw_y = None

    player_x = 0
    player_y = 0

    Enemy_x = 0
    Enemy_y = 0

    kill_Enemy = 0

    player_Hp = 0
    player_MaxHp = 0
    player_Exp = 0
    player_MaxExp = 0
    player_level = 0

    player_super_gaze = 0
    player_super_MAX = 0
    elapsed_time = 0

    def __init__(self, player):
        self.player_x, self.player_y = int(player.x), int(player.y)
        self.player_Hp, self.player_MaxHp = int(player.Hp), int(player.MaxHp)
        self.player_Exp, self.player_MaxExp = int(player.Exp), int(player.MaxExp)
        self.player_super_gaze = player.gauge

        if UI_Manager.UI_Image == None:
            UI_Manager.UI_Image = load_image("assets/Ui/UI.png")

        if UI_Manager.kriby_UI_Image == None:
            UI_Manager.kriby_UI_Image = load_image("assets/Ui/Kirby_UI.png")

        if UI_Manager.Item_Image == None:
            UI_Manager.Item_Image = load_image("assets/Ui/items.png")

        if UI_Manager.UI_font == None:
            UI_Manager.UI_font = load_font("assets/Ui/NEXONFootballGothicL.ttf", 20)
        pass
    def draw(self):
    # 아이템 출력
        self.UI_Image.clip_draw(175, 512 - 98 - 32, 96, 32, 100, 720 - 75, 200, 200 // 3)
    # 경험치 창 출력
        self.UI_Image.clip_draw(374, 512 - 249 - 23, 10, 23, 1280 // 2, 700, 1280, 40)
        self.UI_Image.clip_draw(424, 512 - 189 - 4, 4, 4, 0, 700, round((self.player_Exp / self.player_MaxExp ),4) * 1280 * 2, 28)

    # 필살기 창 출력
        self.UI_Image.clip_draw(374, 512 - 249 - 23, 10, 23, 0 , 500, 100 * 2, 40)
        self.UI_Image.clip_draw(424, 512 - 189 - 4 ,  4,  4,  0, 500, round((self.player_super_gaze /100 ),4) * 100 * 2, 28)
        if self.player_super_gaze >= 100:
            self.UI_font.draw(20, 500, 'READY', (255, 255, 255))

    # 레벨 출력
        self.UI_font.draw(1280 - 100, 720 - 20, '(LEVEL: %d)' % self.player_level, (255, 255, 255))

    # 킬수 출력
        self.UI_font.draw(1280 - 300, 720 - 50, '(KILL: %d)' % self.kill_Enemy, (255, 255, 255))

    # 타이머 출력
        self.UI_font.draw(1280//2 - 60, 720 - 60, '(Time: %3.1f)' % self.elapsed_time, (255, 255, 255))

    # 킬수 출력
        self.UI_font.draw(play_state.kirby_partner_1.sx, play_state.kirby_partner_1.sy + 25, '1', (255, 255, 0))
        self.UI_font.draw(play_state.kirby_partner_2.sx, play_state.kirby_partner_2.sy + 25, '2' , (255, 255, 0))

    # 무기와 방어구 출력
        i = 0
        for weapon in self.Weapons:
            if self.UI_Image == None:
                print(weapon)
                pass
            if weapon == "FIRE":
                self.kriby_UI_Image.clip_draw(0,160 - 32 * 0, 32 , 32, 18+ i * 35, 720 - 56,26,26)
                pass
            elif weapon == "ICE":
                self.kriby_UI_Image.clip_draw(0, 160 - 32 * 1, 32, 32, 18 + i * 35, 720 - 56, 26, 26)
                pass
            elif weapon == "PLASMA":
                self.kriby_UI_Image.clip_draw(0, 160 - 32 * 2, 32, 32, 18 + i * 35, 720 - 56, 26, 26)
                pass
            i +=1
        i = 0
        for accessorie in self.accessories:
            if self.UI_Image == None:
                print(weapon)
                pass
            if accessorie == "ARMOR":
                self.Item_Image.clip_draw(34,  624- 68 - 10 , 14 , 10, 18+ i * 35, 720 - 82,26,26)
                pass
            elif accessorie == "GLOVE":
                self.Item_Image.clip_draw(36, 624 - 469 - 12, 11, 12, 18 + i * 35, 720 - 82, 26, 26)
                pass
            elif accessorie == "WING":
                self.Item_Image.clip_draw(47, 624 - 291 - 14, 14, 14, 18 + i * 35, 720 - 82, 26, 26)
                pass
            i +=1



    def player_UI_update(self, player) :
        self.player_x , self.player_y  = int(player.x), int(player.y)
        self.player_Hp , self.player_MaxHp  = int(player.Hp), int(player.MaxHp)
        self.player_Exp, self.player_MaxExp = int(player.Exp), int(player.MaxExp)
        self.player_super_gaze = player.gauge
        pass

    def update(self, player_x, player_y):
        pass


class enemy_Demage_Draw:
    UI_font = None
    def __init__(self, enemy_sx ,enemy_sy, enemy_height, enemy_demage):
        if enemy_Demage_Draw.UI_font == None:
            enemy_Demage_Draw.UI_font = load_font("assets/Ui/NEXONFootballGothicL.ttf", 20)

        self.durationTimer = 0.5
        self.x = enemy_sx
        self.y = enemy_sy + enemy_height//3
        self.demage = enemy_demage

    def draw(self):
        self.UI_font.draw(self.x, self.y, ('%d')% self.demage, (255, 255, 255))
    def update(self,player_x, player_y):
        self.durationTimer -= game_framework.frame_time
        self.y += 1
        if self.durationTimer <= 0:
            game_world.remove_object(self)
        pass





