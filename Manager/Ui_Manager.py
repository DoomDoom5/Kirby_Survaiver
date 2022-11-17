from pico2d import *

class UI_Manager:
    Weapons = []
    Accessories = []
    UI_Image = None
    Draw_x = None
    Draw_y = None

    player_x = 0
    player_y = 0

    player_Hp = 0
    player_MaxHp = 0

    player_Exp = 0
    player_MaxExp = 0

    def __init__(self):
        if UI_Manager.UI_Image == None:
            UI_Manager.UI_Image = load_image("assets/Ui/UI.png")
        pass
    def draw(self):
        self.UI_Image.clip_draw(280, 512 - 158 - 9, 9, 9, self.player_x, self.player_y - 30, 60, 8)
        self.UI_Image.clip_draw(422, 512 - 158 - 9, 9, 9, self.player_x, self.player_y - 30, self.player_Hp /self.player_MaxHp * 60, 8)
    # 아이템 출력
        self.UI_Image.clip_draw(175, 512 - 98 - 32, 96, 32, 100, 720 - 75, 200, 200 // 3)
    # 경험치 창 출력
        self.UI_Image.clip_draw(374, 512 - 249 - 23, 10, 23, 1280 // 2, 700, 1280, 40)
        self.UI_Image.clip_draw(424, 512 - 189 - 4, 4, 4, 0, 700, (self.player_Exp / self.player_MaxExp) * 1280 * 2, 28)

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

    def player_UI_update(self, player_x, player_y, player_Hp, player_MaxHp, player_Exp, player_MaxExp) :
        self.player_x , self.player_y  = player_x, player_y
        self.player_Hp , self.player_MaxHp  = player_Hp, player_MaxHp
        self.player_Exp, self.player_MaxExp = player_Exp, player_MaxExp
        pass
    def update(self):
        pass