import random
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
            break
        elif ui == 'p':
            game_play()

def game_play():
    comp_board_setup()
    user_board_setup()
    turn()

def comp_board_setup():
    comp_cruiser_placement()
    comp_sub_placement()
    print(comp_board.render())
    print('I have laid out my ships on the grid.\nYou now need to lay out your two ships.\nThe Cruiser is three units long and the Submarine is two units long.')

def comp_cruiser_placement():
    valid_coordinates = random.sample(list(comp_board.cells.keys()), k=3)
    while not comp_board.valid_placement(comp_cruiser, valid_coordinates):
        valid_coordinates = random.sample(list(comp_board.cells.keys()), k=3)
    comp_board.place(comp_cruiser, valid_coordinates)

def comp_sub_placement():
    valid_coordinates = random.sample(list(comp_board.cells.keys()), k=2)
    while not comp_board.valid_placement(comp_sub, valid_coordinates):
        valid_coordinates = random.sample(list(comp_board.cells.keys()), k=2)
    comp_board.place(comp_sub, valid_coordinates)

def user_board_setup():
    user_cruiser_placement()
    user_sub_placement()

def user_cruiser_placement():
    while True:
        ui_coords = input('Enter squares for your Cruiser (3 spaces): ').upper().split()
        if user_board.valid_placement(user_cruiser, ui_coords):
            user_board.place(user_cruiser, ui_coords)
            break
        else:
            print('Those are invalid coordinates. Please try again.')

def user_sub_placement():
    while True:
        ui_coords = input('Enter squares for your Submarine (2 spaces): ').upper().split()
        if user_board.valid_placement(user_sub, ui_coords):
            user_board.place(user_sub, ui_coords)
            break
        else:
            print('Those are invalid coordinates. Please try again.')

def turn():
    global comp_sunk_ships, user_sunk_ships

    print('=============COMPUTER BOARD=============')
    print(comp_board.render())
    print('=============PLAYER BOARD============')
    print(user_board.render(True))

    ui = input('Enter the coordinate for your shot: ').upper()
    if comp_board.valid_coordinate(ui):
        comp_board.cells[ui].fire_upon()
        ui_result = comp_board.cells[ui].render()
        if ui_result == 'X':
            comp_sunk_ships += 1
    else:
        print('Please enter a valid coordinate.')
        turn()
        return

    comp_choice = random.choice(list(user_board.cells.keys()))
    while user_board.cells[comp_choice].is_fired_upon():
        comp_choice = random.choice(list(user_board.cells.keys()))
    user_board.cells[comp_choice].fire_upon()

    comp_result = user_board.cells[comp_choice].render(True)
    if comp_result == 'X':
        user_sunk_ships += 1

    print(f"Your shot on {ui} was a {ui_result}.")
    print(f"My shot on {comp_choice} was a {comp_result}.")

    if game_over():
        return 
    turn()

def game_over():
    if user_sunk_ships == 2:
        print("You can't defeat me you poor excuse for a Sailor!")
        return True
    elif comp_sunk_ships == 2:
        print('I am not a worthy Sailor, for I am but a computer!')
        return True
    return False 



if __name__ == "__main__":
    main()