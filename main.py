def save_game(changes):
    from json import dump
    dump(changes, open('data.json', 'w'), indent=4)
def roll_weapon(current_cash):
    from random import randint, choice
    from json import load
    rarities = {
        "LEGENDARY / ":95, "RARE / ":75, "UNCOMMON / ":50, "COMMON / ":0
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
    weapon = choice(pool)
    save_game({"cash": current_cash-100, "weapon": weapon})
    return weapon
def roll_reforge(current_cash, weapon):
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
    reforge = choice(pool)
    for k, v in reforge.items():
        weapon[k] += v
    save_game({"cash": current_cash - 100, "weapon": weapon})
    return weapon

def fight(weapon, enemy):
    from time import sleep
    if weapon == {}:
        print("No weapon detected! Use \"roll weapon\" to get a new weapon.")
        return
    if enemy['weakness'] == weapon['element']:
        weapon['dmg'] *= enemy['weakness_severity']
    if enemy['strength'] == weapon['element']:
        enemy['dmg'] *= enemy['strength_severity']
    player_health = 100
    while enemy['health'] > 0 and player_health > 0:
        time_left = 100.0
        while time_left > 0.0:
            enemy['health'] -= weapon['dmg']
            print(f"You attacked for {weapon['dmg']} damage!")
            time_cost = (1 / weapon['atkspeed']) * 1000.0
            time_left -= time_cost
            print(f'The attack took {time_cost} seconds to complete!')
            sleep(0.5)
        time_left = 100.0
        
        while time_left > 0.0:
            player_health -= enemy['dmg']
            print(f"The enemy attacked for {enemy['dmg']} damage!")
            time_cost = (1 / enemy['atkspeed']) * 1000.0
            time_left -= time_cost
            print(f'The attack took {time_cost} seconds to complete!')
            sleep(0.5)
    return player_health > int(enemy['health'])

def execute_command(command, *args):
    from json import load, dump
    from random import choice
    data = load(open('data.json', 'r'))
    if command == 'fight':
        fight(load(open("data.json", "r"))['weapon'], choice(load(open("enemies.json", "r"))))
    elif command == 'roll' and data['cash'] >= 100:
        if args[0] == 'weapon':
            roll_weapon(data['cash'])
        elif args[0] == 'reforge':
            roll_reforge(data['cash'], data['weapon'])
    elif command == 'roll' and data['cash'] < 100:
        print("You are too poor. Win some battles to get a new reroll!")
    elif command == 'reset':
        dump({"cash": 200, "weapon": {}}, open("data.json", "w"))
        exit()
    print("new stats:")
    print(load(open('data.json', 'r')))
def main():
    from json import load
    data = load(open("data.json", "r"))
    if data == {"cash": 200, "weapon": {}}:
        print("Welcome to Weapon Simulator! This is a console simulator with multiple weapons and reforges. You have 200 starter cash.\nTo roll a new weapon, type \"roll weapon\". To fight, type \"fight\". You can also \"roll reforge\".")
    else:
        print("Data has been loaded.\nWelcome to Weapon Simulator.")
    while True:
        execute_command(*(input("Enter your command here --> ").split(' ')))
if __name__ == '__main__': 
    main() 