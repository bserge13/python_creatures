import random 

def main():
    while True:
        ui = input("Welcome to BATTLESHIP\nEnter p to play. Enter q to quit. ")
        if ui == 'q':
            print("Come back when you're ready to lose...")
        elif ui == 'p':
            return(game_setup())

def game_setup():
    comp_board_setup()
    user_board_setup()
    turn()
    game_over()

def comp_board_setup():
    ...

def user_board_setup():
    ...

def turn():
    ...

def game_over():
    ...


if __name__ == "__main__":
    main()