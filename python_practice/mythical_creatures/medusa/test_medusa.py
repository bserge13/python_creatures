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

def test_victims_limit():
    medusa = Medusa('Cassiopeia')
    victim1 = Person('Perseus')
    victim2 = Person('Nova')
    victim3 = Person('Loki')
    victim4 = Person('Karl')

    medusa.stare(victim1)
    medusa.stare(victim2)
    medusa.stare(victim3)

    assert len(medusa.statues) == 3
    assert medusa.statues == [victim1, victim2, victim3]

    medusa.stare(victim4)

    assert len(medusa.statues) == 3
    assert medusa.statues == [victim2, victim3, victim4]
    assert victim1.is_stoned() == False
    assert victim4.is_stoned() == True

