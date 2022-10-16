from Character import Enemy
import random



class Enemy_Manager:
    enemys_image = None
    enemy_responTime =10
    Enemys = None

    def __init__(self):
        self.Enemys = [Enemy() for i in range(0, 10)]
        for s_Enemy in self.Enemys:
            s_Enemy.name = "Waddle_dee"
            s_Enemy.x = random.randint(0, 1280)
            s_Enemy.y = random.randint(0, 720)
            s_Enemy.__init__()
            pass

    def respon_Monster(self, Timer):
        if Timer%10 == 0:
            pass

    pass