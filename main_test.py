import main
main.save_game({"cash": 50})
x = main.roll_weapon(150)['weapons'][0]
x['reforge'] = main.roll_reforge(150)
print(x)