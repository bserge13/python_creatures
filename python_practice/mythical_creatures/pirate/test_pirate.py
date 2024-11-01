import pytest 
from pirate import Pirate 

def test_has_name():
    pirate1 = Pirate('Jane')
    pirate2 = Pirate('Blackbeard')

    assert pirate1.name == 'Jane'
    assert pirate2.name == 'Blackbeard'

def test_default_scallywag():
    ...

def test_not_default_cursed():
    ...

def test_has_booty():
    ...

def test_robs_ships():
    ...