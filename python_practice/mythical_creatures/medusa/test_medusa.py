import pytest 
from medusa import Medusa

def test_has_name():
    medusa1 = Medusa('Medusa')
    medusa2 = Medusa('Cassiopeia')

    assert medusa1.name == 'Medusa' 
    assert medusa2.name == 'Cassiopeia'

def test_default_no_statues():
    medusa = Medusa('Cassiopeia')

    assert len(medusa.statues) == 0
    assert medusa.statues == []

def test_gets_statues_staring():
    ...
