import pytest
from vampire import Vampire

def test_has_name():
    vampire1 = Vampire('Brennen')
    vampire2 = Vampire('Dale')

    assert vampire1.name == 'Brennen'
    assert vampire2.name == 'Dale'

def test_has_default_pet():
    vampire = Vampire('Dracula')

    assert vampire.pet == 'bat'
    assert vampire.pet != 'fox'

def test_has_other_pets():
    vampire1 = Vampire('Dracula')
    vampire2 = Vampire('Dimitri', 'fox')

    assert vampire1.pet == 'bat'
    assert vampire2.pet == 'fox'

def test_default_thirsty():
    vampire = Vampire('The Count')

    assert vampire.thirsty == True

def test_quenches_thirst():
    vampire = Vampire('Elizabeth Bathory')

    assert vampire.thirsty == True
    vampire.drink()
    assert vampire.thirsty == False 
