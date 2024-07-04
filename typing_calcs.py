# a monsters type is an object used to get all relationships, the weakness and strength are strings

def mon_weak(mon):
    weaknesses_dict = {}
    for type in mon.type:
        for weakness in type.damage_relations.double_damage_from:
            weakness = weakness.name
            if weakness not in weaknesses_dict:
                weaknesses_dict[weakness] = 1
            else:
                weaknesses_dict[weakness] += 1

    return weaknesses_dict

def mon_weakX2(mon):
    weaknesses = mon_weak(mon)
    X2_list = []
    for weakness in weaknesses:
        if weaknesses[weakness] == 1:
            X2_list.append(weakness)
    
    return X2_list

def mon_weakX4(mon):
    weaknesses = mon_weak(mon)
    X4_list = []
    for weakness in weaknesses:
        if weaknesses[weakness] > 1:
            X4_list.append(weakness)
    
    return X4_list

def mon_strength(mon):
    strengths_dict = {}
    for type in mon.type:
        for strength in type.damage_relations.half_damage_from:
            strength = strength.name
            if strength not in strengths_dict:
                strengths_dict[strength] = 1
            else:
                strengths_dict[strength] += 1

    return strengths_dict

def mon_strengthX2(mon):
    strengths = mon_strength(mon)
    X2_list = []
    for strength in strengths:
        if strengths[strength] == 1:
            X2_list.append(strength)
    
    return X2_list

def mon_strengthX4(mon):
    strengths = mon_strength(mon)
    X4_list = []
    for strength in strengths:
        if strengths[strength] > 1:
            X4_list.append(strength)
    
    return X4_list


def mon_immune(mon):
    immunities = []
    for type in mon.type:
        for imm in type.damage_relations.no_damage_from:
            immunities.append(imm.name)
            
    return immunities