<<<<<<< HEAD
from json import dump
import utils

def save_game(changes):
    json.dump(changes)

def main():
=======
def execute_command(command, *args):
    if command == 'fight':
        fight(*args)
    elif command == 'roll':
        if args[0] == 'weapon':
            roll_weapon(*args[1:])
        elif args[0] == 'reforge':
            roll_reforge(*args[1:])
    elif command == 'respond':
        print(*args)

def main():
    import utils # imports my customized utils module, with a test and timing function. https://GitHub.com/BBernYY/FancyCoding
    from json import load

>>>>>>> 3703392efdc872f1e744a2db5a3b0c31bcd1f21a

if __name__ == '__main__': 
    main() 