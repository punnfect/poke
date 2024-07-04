from monster import Monster

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


