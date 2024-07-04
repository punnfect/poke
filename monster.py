import pokebase as pb
import stat_calcs as sc
import typing_calcs as tc

class Monster:
    def __init__(self, name, lvl, nature, hpIV, atkIV, defIV, spatkIV, spdefIV, speIV, hpEV, atkEV, defEV, spatkEV, spdefEV, speEV):
        print('Catching...')
        self._hold = pb.pokemon(name)
        print(f"You caught a {name}!")
        self.name = name
        self.lvl = lvl
        self.type = []
        for type in self._hold.types:
            self.type.append(type.type)
        self.strength = tc.mon_strengthX2(self)
        self.strengthX4 = tc.mon_strengthX4(self)
        self.weakness = tc.mon_weakX2(self)
        self.weaknessX4 = tc.mon_weakX4(self)
        self.immunity = tc.mon_immune(self)
        self.hp = sc.health_calc(self._hold.stats[0].base_stat, lvl, hpIV, hpEV)
        self.atk = sc.atk_calc(self._hold.stats[1].base_stat, lvl, nature, atkIV, atkEV)
        self.defen = sc.def_calc(self._hold.stats[2].base_stat, lvl, nature, defIV, defEV)
        self.spatk = sc.spatk_calc(self._hold.stats[3].base_stat, lvl, nature, spatkIV, spatkEV)
        self.spdef = sc.spdef_calc(self._hold.stats[4].base_stat, lvl, nature, spdefIV, spdefEV)
        self.speed = sc.speed_calc(self._hold.stats[5].base_stat, lvl, nature, speIV, speEV)
        self.ability = None
        self.move1 = None
        self.move2 = None
        self.move3 = None
        self.move4 = None


    def __str__(self):
        return f"Level {self.lvl} {self.name.capitalize()}."

    def __repr__(self):
        return f"Name {self.name}\nLevel {self.lvl}\nHP Stat {self.hp}\nAtk Stat {self.atk}\
              \nDef Stat {self.defen}\nSpAtk Stat {self.spatk}\nSpDef Stat {self.spdef}\nSpeed Stat {self.speed}\
              \nHalf Dmg {self.strength}\nQuarter Dmg {self.strengthX4}\nDouble Dmg {self.weakness}\nQuadruple Dmg {self.weaknessX4}"