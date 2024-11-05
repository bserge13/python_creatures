import pytest 
from ogre import Ogre, Human

def test_has_name():
    ogre = Ogre('Brak')

    assert ogre.name == 'Brak'

def test_has_default_home():
    ogre1 = Ogre('Brak')
    ogre2 = Ogre('Brak', 'Castle')

    assert ogre1.home == 'Swamp'
    assert ogre2.home == 'Castle'

def test_meets_humans():
    ogre = Ogre('Brak')
    human = Human()

    assert human.name == 'Jane'

    ogre.encounter(human)
    assert ogre.encounter_counter == 1