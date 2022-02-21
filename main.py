def combine_dict(data, changes):
    for k, v in data.items():
        if k in changes:
            if not isinstance(changes[k], str):
                data[k] += changes[k]

def save_game(changes):
    from json import dump, load
    data = load(open('data.json', 'r'))
    data = combine_dict(data, changes)
    dump(data, open('data.json', 'w'), indent=2)

def roll_weapon(current_cash):
    from random import randint, choice
    from json import load
    rarities = {
        "LEGENDARY":95, "RARE":75, "UNCOMMON":50, "COMMON":0
    }
    roll = randint(0, 100)
    for k, v in rarities.items():
        if roll > v:
            rarity = k
            break
    pool = []
    for i in load(open("weapons.json", 'r')).keys():
        if load(open("weapons.json", 'r'))[i]['rarity'] == rarity:
            pool.append(load(open("weapons.json", 'r'))[i])
    return {"cash": current_cash - 100, "weapons": [choice(pool)]}

def roll_reforge(current_cash):
    from random import randint, choice
    from json import load
    rarities = {
        "COMMON":0, "UNCOMMON":50, "RARE":75, "LEGENDARY":95
    }
    roll = randint(0, 100)
    for k, v in rarities.items():
        if roll > v:
            rarity = k
            break
    pool = []
    for i in load(open("reforges.json", 'r')).keys():
        if load(open("reforges.json", 'r'))[i]['rarity'] == rarity:
            pool.append(load(open("reforges.json", 'r'))[i])
    return {"cash": current_cash - 100, "weapons": [choice(pool)]}
    
def execute_command(command, *args):
    if command == 'fight':
        fight(*args)
    elif command == 'roll':
        if args[0] == 'weapon':
            out = roll_weapon(*args[1:])
        elif args[0] == 'reforge':
            out = roll_reforge(*args[1:])
    elif command == 'respond':
        out = " ".join(args)
    return out

def main():
    import utils # imports my customized utils module, with a test and timing function. https://GitHub.com/BBernYY/FancyCoding
    from json import load


if __name__ == '__main__': 
    main() 