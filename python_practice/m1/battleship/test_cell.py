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

def test_render_cell():
    cell1 = Cell('C3')

    assert cell1.render() == '.'
    cell1.fire_upon()
    assert cell1.render() == 'M'

    cell2 = Cell('C3')
    cruiser = Ship('Cruiser', 3)

    cell2.place_ship(cruiser)
    assert cell2.render() == '.'
    assert cell2.render(True) == 'S'
    cell2.fire_upon()
    assert cell2.render() == 'H'
    assert cruiser.is_sunk() == False
    cruiser.hit()
    cruiser.hit()
    assert cruiser.is_sunk() == True
    assert cell2.render() == 'X'