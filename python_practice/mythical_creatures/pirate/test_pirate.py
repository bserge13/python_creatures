import pytest 
from pirate import Pirate 

def test_has_name():
    pirate1 = Pirate('Jane')
    pirate2 = Pirate('Blackbeard')

    assert pirate1.name == 'Jane'
    assert pirate2.name == 'Blackbeard'

def test_default_job():
    pirate1 = Pirate('Jack')
    pirate2 = Pirate('Jeff', 'cook')

    assert pirate1.job == 'Scallywag'
    assert pirate2.job == 'cook'

def test_becomes_cursed():
    pirate = Pirate('James')

    assert pirate.is_cursed() == False
    pirate.commit_heinous_act()
    assert pirate.heinous_count == 1
    assert pirate.is_cursed() == False
    pirate.commit_heinous_act()
    assert pirate.heinous_count == 2
    assert pirate.is_cursed() == False
    pirate.commit_heinous_act()
    assert pirate.is_cursed() == True
    assert pirate.heinous_count == 3

def test_robs_booty_from_ships():
    pirate = Pirate('Jane')

    assert pirate.booty == 0
    pirate.rob_ship()
    assert pirate.booty == 1

    while pirate.booty < 100:
        pirate.rob_ship()

    assert pirate.booty == 100
