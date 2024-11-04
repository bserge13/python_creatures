import pytest 
from medusa import Medusa, Person

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
    medusa = Medusa('Cassiopeia')
    victim = Person('Perseus')

    assert len(medusa.statues) == 0
    assert medusa.statues == []

    medusa.stare(victim)

    assert len(medusa.statues) == 1
    assert medusa.statues == [victim]

def test_victims_turn_stoned():
    medusa = Medusa('Cassiopeia')
    victim = Person('Perseus')

    assert victim.is_stoned() == False
    medusa.stare(victim)
    assert victim.is_stoned() == True