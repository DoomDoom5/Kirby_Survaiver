from pico2d import *

class Item_UI_Manager:
    Weapons = []
    Accessories = []
    Item_UI_Image = None
    Draw_x = None
    Draw_y = None

    def Draw(self):
        for weapon in self.Weapons:
            if weapon == "ICE":
                self.Item_UI_Image.clip_draw(2,624 -265 - 19,27,19,self.Draw_x,self.Draw_y,10,7)
                pass
            elif weapon == "FIRE":
                pass
            elif weapon == "PLASMA":
                pass
