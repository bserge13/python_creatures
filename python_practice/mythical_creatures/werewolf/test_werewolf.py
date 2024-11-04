import pytest 
from werewolf import Werewolf

def test_has_name():
    wolf = Werewolf('David')

    assert wolf.name == 'David'

def test_has_location():
    wolf = Werewolf('David', 'London')

    assert wolf.location == 'London'

def test_default_human():
    wolf = Werewolf('David')

    assert wolf.is_human() == True

def test_can_change_into_werewolf():
    wolf = Werewolf('David')

    assert wolf.is_human() == True
    assert wolf.is_wolf() == False

    wolf.change()

    assert wolf.is_human() == False
    assert wolf.is_wolf() == True

def test_human_changes_back():
    wolf = Werewolf('David')

    assert wolf.is_human() == True
    assert wolf.is_wolf() == False

    wolf.change()

    assert wolf.is_human() == False
    assert wolf.is_wolf() == True

    wolf.change()

    assert wolf.is_human() == True
    assert wolf.is_wolf() == False

def test_werewolf_changes_back():
    wolf = Werewolf('David')

    wolf.change()
    assert wolf.is_wolf() == True

    wolf.change()
    wolf.change()

    assert wolf.is_wolf() == True

def test_default_not_hungry():
    wolf = Werewolf('David')

    assert wolf.is_hungry() == False

def test_hungry_when_changing():
    wolf = Werewolf('David')

    assert wolf.is_hungry() == False

    wolf.change()

    assert wolf.is_wolf() == True
    assert wolf.is_hungry() == True