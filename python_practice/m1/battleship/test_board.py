import pytest 
from board import Board
from cell import Cell
# from ship import Ship

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
