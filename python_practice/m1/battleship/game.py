import random 

def main():
    while True:
        ui = input("Welcome to BATTLESHIP\nEnter p to play. Enter q to quit. ")
        if ui == 'q':
            print("Come back when you're ready to lose...")
        elif ui == 'p':
            return(board_setup())

def board_setup():
    print('so far so good?')

if __name__ == "__main__":
    main()