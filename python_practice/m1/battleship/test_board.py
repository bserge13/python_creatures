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