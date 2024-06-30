import pokebase as pb
import trainer as tr


#initial cache in /home/punnfect/.cache/pokebase

def main():
    pb.cache.set_cache('/home/punnfect/workspace/github.com/punnfect/poke/.cache')
    print(pb.cache.API_CACHE)

    # guy = tr.Trainer("guy")
    # guy.bag.slot1.catch('GaRchomp', 78, 'Adamant', 24, 12, 30, 16, 23, 5, 74, 190, 91, 48, 84, 23)
    # print(guy.bag.slot1.monster)

    # how to get moves
    # moves = pb.pokemon('garchomp')
    # for group in moves.moves[1].version_group_details:
    #     print(group.version_group, group.level_learned_at)
        
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
