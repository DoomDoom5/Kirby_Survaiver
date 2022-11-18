from pico2d import *
from Character import Player

class UI_Manager:
    Weapons = []
    Accessories = []
    UI_Image = None
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

    elapsed_time = 0



    def __init__(self):
        if UI_Manager.UI_Image == None:
            UI_Manager.UI_Image = load_image("assets/Ui/UI.png")

        if UI_Manager.UI_font == None:
            UI_Manager.UI_font = load_font("assets/Ui/NEXONFootballGothicL.ttf", 20)

        pass
    def draw(self):
        self.UI_Image.clip_draw(280, 512 - 158 - 9, 9, 9, self.player_x, self.player_y - 30, 60, 8)
        self.UI_Image.clip_draw(422, 512 - 158 - 9, 9, 9, self.player_x, self.player_y - 30,  round(self.player_Hp / self.player_MaxHp, 3) * 60, 8)
    # 아이템 출력
        self.UI_Image.clip_draw(175, 512 - 98 - 32, 96, 32, 100, 720 - 75, 200, 200 // 3)
    # 경험치 창 출력
        self.UI_Image.clip_draw(374, 512 - 249 - 23, 10, 23, 1280 // 2, 700, 1280, 40)
        self.UI_Image.clip_draw(424, 512 - 189 - 4, 4, 4, 0, 700, round((self.player_Exp / self.player_MaxExp ),3) * 1280 * 2, 28)
    # 레벨 출력
        self.UI_font.draw(1280 - 100, 720 - 20, '(LEVEL: %d)' % self.player_level, (255, 255, 255))

        
    # 킬수 출력
        self.UI_font.draw(1280 - 300, 720 - 50, '(KILL: %d)' % self.kill_Enemy, (255, 255, 255))

    
    # 타이머 출력
        self.UI_font.draw(1280//2, 720 - 100, '(Time: %3.1f)' % self.elapsed_time, (255, 255, 255))
        for weapon in self.Weapons:
            if self.UI_Image == None:
                print(weapon)
                pass
            if weapon == "ICE":
                self.UI_Image.clip_draw(365, 552 - 45 - 24, 24, 24, 10, 600, 20, 20)
                pass
            elif weapon == "FIRE":
                pass
            elif weapon == "PLASMA":
                pass

    def player_UI_update(self, player) :
        self.player_x , self.player_y  = int(player.x), int(player.y)
        self.player_Hp , self.player_MaxHp  = int(player.Hp), int(player.MaxHp)
        self.player_Exp, self.player_MaxExp = int(player.Exp), int(player.MaxExp)
        pass
    def update(self):
        pass