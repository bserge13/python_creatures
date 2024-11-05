import pytest 
from werewolf import Werewolf, Victim

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

def test_consumes_victim():
    wolf = Werewolf('David')
    farmer = Victim()

    assert len(wolf.victims) == 0
    assert wolf.victims == []

    wolf.change()
    wolf.consume_victim(farmer)

    assert len(wolf.victims) == 1
    assert wolf.victims == [farmer]

def test_only_consumes_as_wolf():
    wolf = Werewolf('David')
    farmer = Victim()

    assert len(wolf.victims) == 0
    assert wolf.victims == []

    wolf.consume_victim(farmer)

    assert len(wolf.victims) == 0
    assert wolf.victims == []

def test_not_hungry_after_consume():
    wolf = Werewolf('David')
    farmer = Victim()

    wolf.change()
    wolf.consume_victim(farmer)
    wolf.change()

    assert wolf.is_hungry() == False

def test_victims_dead_after_consumed():
    wolf = Werewolf('David')
    farmer = Victim()

    assert farmer.is_alive() == True

    wolf.change()
    wolf.consume_victim(farmer)
    wolf.change()

    assert farmer.is_alive() == False
