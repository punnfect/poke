from math import floor

def health_calc(base, level, IV=0, EV=0):
    hp = (((2 * base + IV +(EV//4)) * level) // 100) + level + 10
    return hp

def hp_calc(base, level, nature, IV=0, EV=0):
    stat = floor(((((2 * base + IV + (EV//4)) * level) // 100) + 5) * nature)
    return stat

def atk_calc(base, level, nature, IV=0, EV=0):
    if nature in INCATK:
        stat = floor(((((2 * base + IV + (EV//4)) * level) // 100) + 5) * 1.1)
    elif nature in DECATK:
        stat = floor(((((2 * base + IV + (EV//4)) * level) // 100) + 5) * .9)
    else:
        stat = floor(((((2 * base + IV + (EV//4)) * level) // 100) + 5) * 1)
    return stat

def def_calc(base, level, nature, IV=0, EV=0):
    if nature in INCDEF:
        stat = floor(((((2 * base + IV + (EV//4)) * level) // 100) + 5) * 1.1)
    elif nature in DECDEF:
        stat = floor(((((2 * base + IV + (EV//4)) * level) // 100) + 5) * .9)
    else:
        stat = floor(((((2 * base + IV + (EV//4)) * level) // 100) + 5) * 1)
    return stat

def spatk_calc(base, level, nature, IV=0, EV=0):
    if nature in INCSPATK:
        stat = floor(((((2 * base + IV + (EV//4)) * level) // 100) + 5) * 1.1)
    elif nature in DECSPATK:
        stat = floor(((((2 * base + IV + (EV//4)) * level) // 100) + 5) * .9)
    else:
        stat = floor(((((2 * base + IV + (EV//4)) * level) // 100) + 5) * 1)
    return stat

def spdef_calc(base, level, nature, IV=0, EV=0):
    if nature in INCSPDEF:
        stat = floor(((((2 * base + IV + (EV//4)) * level) // 100) + 5) * 1.1)
    elif nature in DECSPDEF:
        stat = floor(((((2 * base + IV + (EV//4)) * level) // 100) + 5) * .9)
    else:
        stat = floor(((((2 * base + IV + (EV//4)) * level) // 100) + 5) * 1)
    return stat

def speed_calc(base, level, nature, IV=0, EV=0):
    if nature in INCSPEED:
        stat = floor(((((2 * base + IV + (EV//4)) * level) // 100) + 5) * 1.1)
    elif nature in DECSPEED:
        stat = floor(((((2 * base + IV + (EV//4)) * level) // 100) + 5) * .9)
    else:
        stat = floor(((((2 * base + IV + (EV//4)) * level) // 100) + 5) * 1)
    return stat

INCATK = ["Lonely", "Adamant", "Naughty", "Brave"]
DECATK = ["Bold", "Modest", "Calm", "Timid"]
INCDEF = ["Bold", "Impish", "Lax", "Relaxed"]
DECDEF = ["Lonley", "Mild", "Gentle", "Hasty"]
INCSPATK = ["Modest", "Mild", "Rash", "Quiet"]
DECSPATK = ["Adamant", "Impish", "Careful", "Jolly"]
INCSPDEF = ["Calm", "Gentle", "Carful", "Sassy"]
DECSPDEF = ["Naughty", "Lax", "Rash", "Naive"]
INCSPEED = ["Timid", "Hasty", "Jolly", "Naive"]
DECSPEED = ["Brave", "Relaxed", "Quiet", "Sassy"]
NEUTRAL = ["Hardy", "Docile", "Bashful", "Quirky", "Serious"] # Not needed