import pytest
from dragon import Dragon 

def test_has_name():
    dragon = Dragon('Ramoth', 'gold', 'Lessa')

    assert dragon.name == 'Ramoth'
    assert dragon.name != 'Lessa'

def test_has_rider():
    dragon = Dragon('Ramoth', 'gold', 'Lessa')

    assert dragon.rider == 'Lessa'
    assert dragon.rider != 'Ramoth'

def test_has_color():
    dragon = Dragon('Ramoth', 'gold', 'Lessa')

    assert dragon.color == 'gold'
    assert dragon.color != 'bronze'

def test_has_name():
    ...

def test_has_name():
    ...

def test_has_name():
    ...

def test_has_name():
    ...

def test_has_name():
    ...