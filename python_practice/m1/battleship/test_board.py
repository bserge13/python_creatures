import pytest 
from board import Board
from cell import Cell
from ship import Ship

board = Board()
cruiser = Ship('Cruiser', 3)
submarine = Ship('Submarine', 2)

def test_class_attrs():
    assert hasattr(board, 'cells')
    assert isinstance(board.cells, dict)
    assert isinstance(board.cells['A1'], Cell)
    assert len(board.cells) == 16

def test_valid_coordinate():
    assert board.valid_coordinate('A1') == True
    assert board.valid_coordinate('D4') == True
    assert board.valid_coordinate('A5') == False
    assert board.valid_coordinate('E1') == False
    assert board.valid_coordinate('A22') == False

def test_valid_placement_length():
    coordinates1 = ['A1', 'A2']
    coordinates2 = ['A2', 'A3', 'A4']

    assert board.valid_placement(cruiser, coordinates1) == False
    assert board.valid_placement(submarine, coordinates2) == False

    assert board.valid_placement(cruiser, coordinates2) == True
    assert board.valid_placement(submarine, coordinates1) == True

def test_valid_placement_consecutive():
    coordinates1 = ['A1', 'A2', 'A4']
    coordinates2 = ['A1', 'C1']
    coordinates3 = ['A3', 'A2', 'A1']
    coordinates4 = ['C1', 'B1']

    assert board.valid_placement(cruiser, coordinates1) == False
    assert board.valid_placement(submarine, coordinates2) == False
    assert board.valid_placement(cruiser, coordinates3) == False
    assert board.valid_placement(submarine, coordinates4) == False

def test_valid_placement_diagonal():
    coordinates1 = ['A1', 'B2', 'C3']
    coordinates2 = ['C2', 'D3']

    assert board.valid_placement(cruiser, coordinates1) == False
    assert board.valid_placement(submarine, coordinates2) == False

def test_valid_placement_passing():
    coordinates1 = ['B1', 'C1', 'D1']
    coordinates2 = ['A1', 'A2']

    assert board.valid_placement(cruiser, coordinates1) == True
    assert board.valid_placement(submarine, coordinates2) == True

def test_place_ship():
    cell1 = board.cells['A1']
    cell2 = board.cells['A2']
    cell3 = board.cells['A3']

    board.place(cruiser, ['A1', 'A2', 'A3'])

    assert cell1.ship == cruiser
    assert cell2.ship == cruiser
    assert cell3.ship == cruiser
    assert cell3.ship == cell2.ship

def test_overlapping_ships():
    board.place(cruiser, ['A1', 'A2', 'A3'])

    assert board.valid_placement(submarine, ['A1', 'B1']) != True
    assert board.valid_placement(submarine, ['A1', 'B1']) == False

def test_render_board():
    board.place(cruiser, ['A1', 'A2', 'A3'])

    assert board.render() == "  1 2 3 4 \nA . . . . \nB . . . . \nC . . . . \nD . . . . \n"
    assert board.render(True) ==  "  1 2 3 4 \nA S S S . \nB . . . . \nC . . . . \nD . . . . \n"