import pytest 
from board import Board
from cell import Cell
from ship import Ship

cruiser = Ship('Cruiser', 3)
submarine = Ship('Submarine', 2)

def test_class_attrs():
    board = Board()

    assert hasattr(board, 'cells')
    assert isinstance(board.cells, dict)
    assert isinstance(board.cells['A1'], Cell)
    assert len(board.cells) == 16

def test_valid_coordinate():
    board = Board()

    assert board.valid_coordinate('A1') == True
    assert board.valid_coordinate('D4') == True
    assert board.valid_coordinate('A5') == False
    assert board.valid_coordinate('E1') == False
    assert board.valid_coordinate('A22') == False

def test_valid_placement_length():
    board = Board()

    coordinates1 = ['A1', 'A2']
    coordinates2 = ['A2', 'A3', 'A4']

    assert board.valid_placement(cruiser, coordinates1) == False
    assert board.valid_placement(submarine, coordinates2) == False

    assert board.valid_placement(cruiser, coordinates2) == True
    assert board.valid_placement(submarine, coordinates1) == True

def test_valid_placement_consecutive():
    board = Board()

    coordinates1 = ['A1', 'A2', 'A4']
    coordinates2 = ['A1', 'C1']
    coordinates3 = ['A3', 'A2', 'A1']
    coordinates4 = ['C1', 'B1']

    assert board.valid_placement(cruiser, coordinates1) == False
    assert board.valid_placement(submarine, coordinates2) == False
    assert board.valid_placement(cruiser, coordinates3) == False
    assert board.valid_placement(submarine, coordinates4) == False

def test_valid_placement_diagonal():
    board = Board()

    coordinates1 = ['A1', 'B2', 'C3']
    coordinates2 = ['C2', 'D3']

    assert board.valid_placement(cruiser, coordinates1) == False
    assert board.valid_placement(submarine, coordinates2) == False

def test_valid_placement_passing():
    board = Board()

    coordinates1 = ['B1', 'C1', 'D1']
    coordinates2 = ['A1', 'A2']

    assert board.valid_placement(cruiser, coordinates1) == True
    assert board.valid_placement(submarine, coordinates2) == True

def test_place_ship():
    board = Board()

    cell1 = board.cells['A1']
    cell2 = board.cells['A2']
    cell3 = board.cells['A3']

    board.place(cruiser, ['A1', 'A2', 'A3'])

    assert cell1.ship == cruiser
    assert cell2.ship == cruiser
    assert cell3.ship == cruiser
    assert cell3.ship == cell2.ship

def test_overlapping_ships():
    board = Board()

    board.place(cruiser, ['A1', 'A2', 'A3'])

    assert board.valid_placement(submarine, ['A1', 'B1']) != True
    assert board.valid_placement(submarine, ['A1', 'B1']) == False

def test_render_board_placement():
    board1 = Board()
    board2 = Board()

    board1.place(cruiser, ['A1', 'A2', 'A3'])
    board2.place(submarine, ['C3', 'D3'])

    assert board1.render() == "  1 2 3 4 \nA . . . . \nB . . . . \nC . . . . \nD . . . . \n"
    assert board1.render(True) ==  "  1 2 3 4 \nA S S S . \nB . . . . \nC . . . . \nD . . . . \n"

    assert board2.render() == "  1 2 3 4 \nA . . . . \nB . . . . \nC . . . . \nD . . . . \n"
    assert board2.render(True) ==  "  1 2 3 4 \nA . . . . \nB . . . . \nC . . S . \nD . . S . \n"

def test_render_board_miss():
    board = Board()

    board.place(cruiser, ['A1', 'A2', 'A3'])
    assert board.render(True) ==  "  1 2 3 4 \nA S S S . \nB . . . . \nC . . . . \nD . . . . \n"

    board.cells['A4'].fire_upon()
    board.cells['C3'].fire_upon()
    board.cells['D1'].fire_upon()
    assert board.render(True) ==  "  1 2 3 4 \nA S S S M \nB . . . . \nC . . M . \nD M . . . \n"

def test_render_board_hit():
    board = Board()

    board.place(cruiser, ['B3', 'C3', 'D3'])
    assert board.render(True) ==  "  1 2 3 4 \nA . . . . \nB . . S . \nC . . S . \nD . . S . \n"

    coordinates = ['A3', 'B3', 'C3']
    for coord in coordinates:
        board.cells[coord].fire_upon()

    assert board.render(True) ==  "  1 2 3 4 \nA . . M . \nB . . H . \nC . . H . \nD . . S . \n"
