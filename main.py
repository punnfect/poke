import pokebase as pb
import trainer as tr
import typing_calcs as ty



def main():
    pb.cache.set_cache('../.cache')
    print(pb.cache.API_CACHE)

    guy = tr.Trainer("guy")
    guy.bag.slot1.catch('GaRchomp', 78, 'Adamant', 24, 12, 30, 16, 23, 5, 74, 190, 91, 48, 84, 23)
    print(guy.bag.slot1.monster.move1.name)
    # print(ty.mon_strengthX2(guy.bag.slot1.monster))
    mud = 'mud-shot'
    # how to get moves
    # moves = pb.pokemon('garchomp')
    # print(moves.types[1].type.damage_relations.double_damage_from)
    # guy.bag.slot1.monster.move1.set_move(mud)
    guy.bag.slot1.monster.ability.set_ability("sand-veil")
    print(guy.bag.slot1.monster.ability)
    # for group in guy.bag.slot1.monster._hold.moves:
    #     print(group.move)
        
    # names for every pokemon
    # names = pb.APIResourceList('pokemon')
    # for name in names:
    #     print(name["name"])



    # chesto = pb.APIResource('berry', 'chesto')
    # print(chesto.natural_gift_type.name)

    # char = pb.pokemon('squirtle')
    # print(char.abilities[0].ability.effect_entries[1].short_effect)


    # print(char.stats[0].stat.name, char.stats[0].base_stat)


main()
