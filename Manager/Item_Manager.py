import random

import game_framework
import game_world
import math
from pico2d import *



class Item:
    Name = None
    Gained = None
    x = 0
    y = 0
class ExpStone(Item):
    Type = None
    Exp = None
    Magnet = None
    def __init__(self,Enemy_x=0, Enemy_y=0):
        self.width = 12
        self.height = 18
        self.Magnet = False
        self.Gained = False
        self.x = Enemy_x
        self.y = Enemy_y
        self.Name = "EXP_STONE"
        self.t = 0.0
        match self.Type:
            case "GREEN":
                self.Exp = 2
            case "BLUE":
                self.Exp = 5
            case "RED":
                self.Exp = 10
            case "YEELOW":
                self.Exp = 20

    def Magnet_Player(self, Player_x=0, Player_y=0, Player_Magnet_Range=0):
        if self.Magnet:
            gainRange = 2
            self.t += 0.01
            self.x = (1-self.t) * self.x+ self.t * Player_x
            self.y = (1-self.t) * self.y+ self.t * Player_y
            if self.x - self.width//2 < Player_x - gainRange \
                    and self.y - self.height//2 < Player_y - gainRange\
                    and self.x + self.width//2 > Player_x + gainRange\
                    and self.y + self.height//2 > Player_y + gainRange:
                self.Gained = True
            
        else:
            if self.x  > Player_x - Player_Magnet_Range \
                    and self.y > Player_y - Player_Magnet_Range \
                    and self.x < Player_x + Player_Magnet_Range \
                    and self.y < Player_y + Player_Magnet_Range : # 마그넷 충돌 검사
                self.Magnet = True


    def Draw(self, Item_Image):
        match self.Type:
            case "GREEN":
                Item_Image.clip_draw(51, 624 - 96 - 12, 9,12,self.x,self.y,self.width, self.height)
            case "BLUE":
                Item_Image.clip_draw(51, 624 - 36 - 12, 9, 12, self.x, self.y,self.width, self.height)
            case "RED":
                Item_Image.clip_draw(51, 624 - 526 - 12, 9, 12, self.x, self.y,self.width, self.height)
        pass

class Item_manager:
    Items = []
    Items_image = None
    expStone = ExpStone()
    def __init__(self):
        if Item_manager.Items_image == None:
            Item_manager.Items_image = load_image("assets/Ui/items.png")

    def Create_EXP_Stone(self, Enemy_crystal, Enemy_x, Enemy_y):
        newExpStone = ExpStone()
        newExpStone.Type = Enemy_crystal
        newExpStone.__init__(Enemy_x,Enemy_y)
        self.Items.append(newExpStone)
        del newExpStone

    def draw(self):
        for item in self.Items:
            match item.Name:
                case "EXP_STONE":
                    self.expStone = item
                    self.expStone.Draw(self.Items_image)

    def update(self, player_x, player_y):
        pass

    def GainExp(self, Player_x, Player_y, Player_Magnet_Range, Player_Exp):
        for item in self.Items:
            if item.Gained:
                self.Items.remove(item)
            else:
                match item.Name :
                    case "EXP_STONE":
                        self.expStone = item
                        self.expStone.Magnet_Player(Player_x, Player_y, Player_Magnet_Range)
                        if item.Gained:
                            Player_Exp = self.expStone.Exp
                            self.Items.remove(item)
                            return self.expStone.Exp

        return 0




