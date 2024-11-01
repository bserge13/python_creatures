import pytest 
from hobbit import Hobbit

def test_has_name():
    hobbit1 = Hobbit('Bilbo')
    hobbit2 = Hobbit('Peregrin')

    assert hobbit1.name == 'Bilbo'
    assert hobbit2.name == 'Peregrin'

def test_default_dispositions():
    hobbit1 = Hobbit('Samwise')
    hobbit2 = Hobbit('Frodo', 'adventurous')

    assert hobbit1.disposition == 'homebody'
    assert hobbit2.disposition == 'adventurous'

def test_grows_older():
    hobbit = Hobbit('Pippen')

    assert hobbit.age == 0

    for _ in range(5):
        hobbit.celebrate_birthday()

    assert hobbit.age == 5

def test_is_adult():
    hobbit = Hobbit('Mary')

    for _ in range(32):
        hobbit.celebrate_birthday()

    assert hobbit.age == 32
    assert hobbit.is_adult() == False
    hobbit.celebrate_birthday()
    assert hobbit.age == 33
    assert hobbit.is_adult() == True

def test_is_old():
    hobbit = Hobbit('Loki', 'Scardy Cat', 100)

    assert hobbit.is_old() == False
    assert hobbit.age == 100
    hobbit.celebrate_birthday()
    assert hobbit.age == 101
    assert hobbit.is_old() == True

def test_has_ring():
    hobbit1 = Hobbit('Samwise')
    hobbit2 = Hobbit('Frodo')

    assert hobbit1.has_ring() == False
    assert hobbit2.has_ring() == True

def test_is_short():
    hobbit = Hobbit('Karl')

    assert hobbit.is_short() == True