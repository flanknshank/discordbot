import random
attacks = {
    "kiwi": {
        "Bamboozlered" : 49,
        "hits" : 5,
        "kicked" : 7,
        "squidbagged" : 12,
        "tenta missiles" : 20,
        "aimdrills" : 13,
        "poke" : 2,
        "burst bomb" : 10,
        "line marker" : 5,
        "steals okane" : 17
    },
    "henlo" : {
        "subway" : 54,
        "wiper" : 15,
        "poke" : 2,
        "tenta missiles" : 20,
        "disbands sonder" : 14,
        "learns squeezer" : 7,
        "hits" : 5,
        "kicked" : 7,
        "Steals your SQ points" : 17,
        "this way!" : 10
    }, 
    "Jay" : {
        "tri-slosher" : 22,
        "9 iron" : 40,
        "actual knife" : 7,
        "feed" : 10,
        "frontline jr" : 30, #varies between -50 to 30
        "war crime" : 14,
        "literally a pencil" : 3,
        "golf cart" : 26,
        "mist spam" : 2,
        "spawncamp" : 16
    },
    "Riki" : {
        "Squeezer aimbot" : 9999,

    }
}

def select_move(person):
    move = random.choice(list(attacks[person].keys()))
    damage = attacks[person][move]
    return move, damage
