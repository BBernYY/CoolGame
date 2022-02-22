import main
from json import load
enemy = {
        "display_name": "Molten",
        "dmg": 25,
        "weakness": "WATER",
        "weakness_severity": 1.5,
        "health": 500,
        "atkspeed": 35,
        "strength": "FIRE",
        "strength_severity": 0.75
    }

print(main.fight(main.roll_reforge(400, main.roll_weapon(500)), enemy))