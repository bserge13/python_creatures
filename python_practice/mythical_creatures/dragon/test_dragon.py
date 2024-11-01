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

def test_default_hungry():
    dragon = Dragon('Mnementh', 'bronze', 'Flar')

    assert dragon.is_hungry() == True

def test_gets_full_eating():
    dragon = Dragon('Mnementh', 'bronze', 'Flar')

    assert dragon.is_hungry() == True
    dragon.eat()
    assert dragon.is_hungry() == True
    dragon.eat()
    assert dragon.is_hungry() == True
    dragon.eat()
    assert dragon.is_hungry() == False

def test_hungry_after_sleep():
    dragon = Dragon('Mnementh', 'bronze', 'Flar')

    assert dragon.is_hungry() == True
    dragon.eat()
    assert dragon.is_hungry() == True
    dragon.eat()
    assert dragon.is_hungry() == True
    dragon.eat()
    assert dragon.is_hungry() == False
    dragon.sleep()
    assert dragon.is_hungry() == True