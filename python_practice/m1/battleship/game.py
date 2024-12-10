from random import sample, choice
from board import Board
from ship import Ship

comp_board = Board()
comp_cruiser = Ship('Cruiser', 3)
comp_sub = Ship('Submarine', 2)
comp_sunk_ships = 0 

user_board = Board() 
user_cruiser = Ship('Cruiser', 3)
user_sub = Ship('Submarine', 2)
user_sunk_ships = 0

def main():
    while True:
        ui = input('Welcome to BATTLESHIP\nEnter p to play. Enter q to quit. ')
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
    print('=============COMPUTER BOARD=============')
    print(comp_board.render())
    print('=============PLAYER BOARD============')
    print(user_board.render(True))
    ui = input('Enter the coordinate for your shot:').upcase()
    if comp_board.valid_coordinate(ui):
        comp_board.cells[ui].fire_upon()
        ui_result = comp_board.cells[ui].render()
        if ui_result == 'X':
            comp_sunk_ships += 1
    else:
        print('Please enter a valid coordinate.')
        turn()

    comp_choice = choice(user_board.cells)
    while user_board.cells[comp_choice].is_fired_upon() == False:
        comp_choice = choice(user_board.cells)
    user_board.cells[comp_choice].fire_upon()

    comp_result = user_board.cells[comp_choice].render(True)
    if comp_result == 'X':
        user_sunk_ships += 1
    print(f"Your shot on {ui} was a {ui_result}.")
    print(f"My shot on {comp_choice} was a {comp_result}.")
    game_over()

def game_over():
    if user_sunk_ships == 2:
        print("You can't defeat me you poor excuse for a Sailor!")
    elif comp_sunk_ships == 2:
        print('I am not a worthy Sailor, for I am but a computer!')
    else:
        turn()



if __name__ == "__main__":
    main()