import pytest 
from cell import Cell
from ship import Ship

def test_cell_class_attrs():
    cell = Cell('B4')

    assert cell.coordinate == 'B4'
    assert cell.ship == None
    assert cell.is_empty() == True

def test_place_ship():
    cell = Cell('B4')
    cruiser = Ship('Cruiser', 3)

    cell.place_ship(cruiser)
    assert cell.ship == cruiser
    assert cell.is_empty() == False