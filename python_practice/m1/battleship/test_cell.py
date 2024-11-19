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

def test_fired_upon():
    cell = Cell('B4')
    cruiser = Ship('Cruiser', 3)

    cell.place_ship(cruiser)
    assert cell.is_fired_upon() == False

    cell.fire_upon()
    assert cell.ship.health == 2
    assert cell.is_fired_upon() == True