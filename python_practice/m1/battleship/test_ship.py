import pytest 
from ship import Ship

def test_ship_class():
    cruiser = Ship('Cruiser', 3)

    assert cruiser.name == 'Cruiser'
    assert cruiser.length == 3
    assert cruiser.health == 3 
    assert cruiser.is_sunk() == False

    cruiser.hit()
    assert cruiser.health == 2

    cruiser.hit()
    assert cruiser.health == 1
    assert cruiser.is_sunk() == False

    cruiser.hit()
    assert cruiser.health == 0
    assert cruiser.is_sunk() == True