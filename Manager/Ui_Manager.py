from pico2d import *

class Item_UI_Manager:
    Weapons = []
    Accessories = []
    Item_UI_Image = None

    def Draw(self):
        for weapon in self.Weapons:
            if weapon == "ICE":
                pass
            elif weapon == "FIRE":
                pass
            elif weapon == "PLASMA":
                pass
