import random
attacks = {
    "kiwi": {
        "Bamboozler" : 49,
        "punch" : 5,
        "kick" : 7,
        "squidbagg" : 17,
        "tenta missiles" : 22,
        "aimdrills" : 13,
        "poke" : 2,
        "burst bomb" : 20,
        "line marker" : 10,
        "steals okane" : 17
    },
    "henlo" : {
        "subway" : 54,
        "wiper" : 15,
        "poke" : 2,
        "tenta missiles" : 20,
        "disbands sonder" : 14,
        "learns squeezer" : 7,
        "punch" : 5,
        "kick" : 7,
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
        "Squeezer aimbot" : 43,
        "Coding til 3am" : 23,
        "touching grass" : 23,
        "outfrags you" : 21,
        "H3D" : 12,
        "hugs you" : -20,
        "leetcode" : 12,
        "poke" : 2,
        "punch" : 8,
        "rikichar" : 7

    },
    "Splatbot" : {
        "Aimbot.exe" : 40,
        "bubblesort" : -100,
        "AI art" : 30,
        "hacking" : 42,
        "laggy internet" :27,
        "exploits" : 36
    }
}

def select_move(person):
    move = random.choice(list(attacks[person].keys()))
    damage = attacks[person][move]
    return move, damage
