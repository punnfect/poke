import pokebase as pb
import trainer as tr


#initial cache in /home/punnfect/.cache/pokebase

def main():
    pb.cache.set_cache('/home/punnfect/workspace/github.com/punnfect/poke/.cache')
    print(pb.cache.API_CACHE)

    guy = tr.Trainer("guy")
    guy.bag.slot1 = tr.Ball(tr.Monster('garchomp', 78))
    print(guy.bag.slot1.monster.name)
    print(guy.bag.slot1.monster.lvl)
    print(guy.bag.slot1.monster.hp)
    print(guy.bag.slot1.monster.atk)
    print(guy.bag.slot1.monster.defen)
    print(guy.bag.slot1.monster.spatk)
    print(guy.bag.slot1.monster.spdef)
    print(guy.bag.slot1.monster.speed)



    # chesto = pb.APIResource('berry', 'chesto')
    # print(chesto.natural_gift_type.name)

    # char = pb.pokemon('squirtle')
    # print(char.abilities[0].ability.effect_entries[1].short_effect)


    # print(char.stats[0].stat.name, char.stats[0].base_stat)


main()
