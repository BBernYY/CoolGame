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




if __name__ == '__main__': # checks if the code is ran as a file
    main() # starts the main function
