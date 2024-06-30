import pokebase as pb
import stat_calcs as sc

class Trainer:
    def __init__(self, name):
        self.name = name
        self.bag = Bag()
    
class Bag:
    def __init__(self):
        self.slot1 = Ball()
        self.slot2 = Ball()
        self.slot3 = Ball()
        self.slot4 = Ball()
        self.slot5 = Ball()
        self.slot6 = Ball()

class Ball:
    def __init__(self, monster=None):
        self.monster = monster

class Monster:
    def __init__(self, name, lvl, nature=1):
        self._hold = pb.pokemon(name)
        self.name = name
        self.lvl = lvl
        self.hp = sc.health_calc(self._hold.stats[0].base_stat, lvl, 24,74)
        self.atk = sc.atk_calc(self._hold.stats[1].base_stat, lvl, nature, 12, 190)
        self.defen = sc.def_calc(self._hold.stats[2].base_stat, lvl, nature, 30, 91)
        self.spatk = sc.spatk_calc(self._hold.stats[3].base_stat, lvl, nature, 16, 48)
        self.spdef = sc.spdef_calc(self._hold.stats[4].base_stat, lvl, nature, 23, 84)
        self.speed = sc.speed_calc(self._hold.stats[5].base_stat, lvl, nature, 5, 23)