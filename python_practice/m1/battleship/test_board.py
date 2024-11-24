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

# def test_valid_placement_consecutive():
#     coordinates1 = ['A1', 'A2', 'A4']
#     coordinates2 = ['A1', 'C1']
#     coordinates3 = ['A3', 'A2', 'A1']
#     coordinates4 = ['C1', 'B1']

#     assert board.valid_placement(cruiser, coordinates1) == False
#     assert board.valid_placement(submarine, coordinates2) == False
#     assert board.valid_placement(cruiser, coordinates3) == False
#     assert board.valid_placement(submarine, coordinates4) == False

# def test_valid_placement_diagonal():
#     coordinates1 = ['A1', 'B2', 'C3']
#     coordinates2 = ['C2', 'D3']

#     assert board.valid_placement(cruiser, coordinates1) == False
#     assert board.valid_placement(submarine, coordinates2) == False
