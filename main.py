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
def roll_reforge(current_cash, weapon_name):
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
    for v in load(open("weapons.json", "r")).values():
        if v['display_name'] == weapon_name:
            weapon = v
            break
    for k, v in reforge.items():
        weapon[k] += v
    save_game({"cash": current_cash - 100, "weapon": weapon})
    return weapon

def fight(weapon, enemy, starting_cash):
    from time import sleep
    from json import dump
    if weapon == {}:
        print("No weapon detected! Use \"roll weapon\" to get a new weapon.")
        return
    print("This is your matchup:\n")
    sleep(1)
    print(enemy)
    sleep(3)
    if enemy['weakness'] == weapon['element']:
        weapon['dmg'] *= enemy['weakness_severity']
    if enemy['strength'] == weapon['element']:
        enemy['dmg'] *= enemy['strength_severity']
    player_health = 100
    print("\n\n\nThe battle starts!\n\n")
    sleep(1)
    while enemy['health'] > 0 and player_health > 0:
        time_left = 100.0
        hits = 0
        while time_left > 0.0:
            enemy['health'] -= weapon['dmg']
            time_cost = (1 / weapon['atkspeed']) * 1000.0
            time_left -= time_cost
            hits += 1
        time_left = 100.0 - weapon['stun'] / 50
        print(f"You hit {hits} times with a damage of {weapon['dmg']}! The enemy now has {enemy['health']} health left.")
        hits = 0
        sleep(2)
        while time_left > 0.0:
            player_health -= enemy['dmg']
            time_cost = (1 / enemy['atkspeed']) * 1000.0
            time_left -= time_cost
            hits += 1
        print(f"\n\nThe enemy hit you {hits} times with a damage of {enemy['dmg']}! You now have {player_health} health left.")
        sleep(2)
    if player_health > int(enemy['health']):
        print("\n\nYou won! you got 20 cash.")
    else:
        print("\n\nYou lost...")
    sleep(1)
    dump({"weapon": weapon, "cash": starting_cash + 20}, open('data.json', 'w'))

def execute_command(command, *args):
    from json import load, dump
    from random import choice
    data = load(open('data.json', 'r'))
    if command == 'fight':
        fight(load(open("data.json", "r"))['weapon'], choice(load(open("enemies.json", "r"))['enemies']), data['cash'])
    elif command == 'roll' and data['cash'] >= 100:
        if args[0] == 'weapon':
            roll_weapon(data['cash'])
        elif args[0] == 'reforge':
            roll_reforge(data['cash'], data['weapon']['display_name'])
    elif command == 'roll' and data['cash'] < 100:
        print("You are too poor. Win some battles to get a new reroll!")
    elif command == 'reset':
        dump({"cash": 200, "weapon": {}}, open("data.json", "w"))
        exit()
    print("\n\nnew stats:\n\n")
    print(load(open('data.json', 'r')))
def main():
    from json import load
    data = load(open("data.json", "r"))
    if data == {"cash": 200, "weapon": {}}:
        print("Welcome to Weapon Simulator! This is a console simulator with multiple weapons and reforges. You have 200 starter cash.\nTo roll a new weapon, type \"roll weapon\". To fight, type \"fight\". You can also \"roll reforge\".")
    else:
        print("Data has been loaded.\nWelcome to Weapon Simulator.")
    while True:
        execute_command(*(input("\n\nEnter your command here --> ").split(' ')))
if __name__ == '__main__': 
    main()