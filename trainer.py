import pokebase as pb
import stat_calcs as sc

# each trainer has a Bag() initialized to 6 empty Ball()s. Each ball will catch() a monster with name, lvl, nature, IV, EV

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
    def __init__(self):
        self.monster = None
        self.type = "pokeball"

    def set_ball_type(self, type):
        self.type = type

    def catch(self, monster, lvl, nature, hpIV, atkIV, defIV, spatkIV, spdefIV, speIV, hpEV, atkEV, defEV, spatkEV, spdefEV, speEV):
        self.monster = Monster(monster.lower(), lvl, nature, hpIV, atkIV, defIV, spatkIV, spdefIV, speIV, hpEV, atkEV, defEV, spatkEV, spdefEV, speEV)

class Monster:
    def __init__(self, name, lvl, nature, hpIV, atkIV, defIV, spatkIV, spdefIV, speIV, hpEV, atkEV, defEV, spatkEV, spdefEV, speEV):
        print('Catching...')
        self._hold = pb.pokemon(name)
        print(f"You caught a {name}!")
        self.name = name
        self.lvl = lvl
        self.hp = sc.health_calc(self._hold.stats[0].base_stat, lvl, hpIV, hpEV)
        self.atk = sc.atk_calc(self._hold.stats[1].base_stat, lvl, nature, atkIV, atkEV)
        self.defen = sc.def_calc(self._hold.stats[2].base_stat, lvl, nature, defIV, defEV)
        self.spatk = sc.spatk_calc(self._hold.stats[3].base_stat, lvl, nature, spatkIV, spatkEV)
        self.spdef = sc.spdef_calc(self._hold.stats[4].base_stat, lvl, nature, spdefIV, spdefEV)
        self.speed = sc.speed_calc(self._hold.stats[5].base_stat, lvl, nature, speIV, speEV)
        self.move1 = None
        self.move2 = None
        self.move3 = None
        self.move4 = None

    def __repr__(self):
        return f"Name {self.name}\nLevel {self.lvl}\nHP Stat {self.hp}\nAtk Stat {self.atk}\
              \nDef Stat {self.defen}\nSpAtk Stat {self.spatk}\nSpDef Stat {self.spdef}\nSpeed Stat {self.speed}"
