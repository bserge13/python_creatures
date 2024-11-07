import pytest 
from direwolf import Direwolf, Stark

def test_has_name():
    wolf = Direwolf('Lady')

    assert wolf.name == 'Lady'

def test_default_home():
    wolf1 = Direwolf('Ghost')
    wolf2 = Direwolf('Lady', 'Kings Landing')

    assert wolf1.home == 'Beyond the Wall'
    assert wolf2.home == 'Kings Landing'

def test_default_size():
    wolf1 = Direwolf('Ghost')
    wolf2 = Direwolf('Shaggydog', 'Winterfell', 'Smol Pupper')

    assert wolf1.size == 'Massive'
    assert wolf2.size == 'Smol Pupper'

def test_stark_default_location():
    wolf = Direwolf('Summer', 'Winterfell')
    stark = Stark('Bran')

    assert wolf.home == 'Winterfell'
    assert stark.location == 'Winterfell'

def test_protects_starks():
    wolf = Direwolf('Nymeria', 'Riverlands')
    stark = Stark('Arya', 'Riverlands')

    assert wolf.starks_to_protect() == []
    wolf.protect(stark)
    assert wolf.starks_to_protect() == [stark]

def test_same_location_to_protect():
    wolf = Direwolf('Ghost')
    stark = Stark('Jon', 'Kings Landing')

    wolf.protect(stark)
    assert wolf.starks_to_protect() == []

def test_protects_two_at_a_time():
    wolf1 = Direwolf('Summer', 'Winterfell')
    wolf2 = Direwolf('Lady', 'Winterfell')
    sansa = Stark('Sansa')
    jon = Stark('Jon')
    rob = Stark('Rob')
    bran = Stark('Bran')
    arya = Stark('Arya')

    wolf1.protect(sansa)
    wolf1.protect(jon)

    wolf2.protect(rob)
    wolf2.protect(bran)
    wolf2.protect(arya)

    assert wolf1.starks_to_protect() == [sansa, jon]
    assert wolf2.starks_to_protect() == [rob, bran]
    assert wolf2.starks_to_protect() != [rob, bran, arya]

def test_default_stark_attr():
    arya = Stark('Arya')
    sansa = Stark('Sansa')

    assert sansa.house_words == 'Winter is coming'
    assert arya.is_safe() == False

def test_starks_safety_changes():
    wolf = Direwolf('Nymeria', 'Winterfell')
    arya = Stark('Arya')

    assert arya.is_safe() == False
    wolf.protect(arya)
    assert arya.is_safe() == True

def test_default_hunts_walkers():
    wolf = Direwolf('Loki')
    assert wolf.hunts_walkers() == True

def test_no_hunt_while_protecting():
    wolf = Direwolf('Nymeria', 'Winterfell')
    arya = Stark('Arya')

    assert wolf.hunts_walkers() == True
    assert arya.is_safe() == False
    wolf.protect(arya)
    assert arya.is_safe() == True
    assert wolf.hunts_walkers() == False

def test_stops_protecting_and_returns_stark_object():
    wolf1 = Direwolf('Summer', 'Winterfell')
    wolf2 = Direwolf('Lady', 'Winterfell')
    sansa = Stark('Sansa')
    arya = Stark('Arya')

    wolf1.protect(arya)
    wolf2.protect(sansa)
    assert wolf1.hunts_walkers() == False

    wolf1.leave(arya)

    assert wolf1.starks_to_protect() == []
    assert wolf2.starks_to_protect() == [sansa]
    assert wolf1.hunts_walkers() == True


def test_returns_stark_object_when_leaving():
    wolf = Direwolf('Summer', 'Winterfell')
    arya = Stark('Arya')

    wolf.protect(arya)
    expected = wolf.leave(arya)

    assert expected == arya
    assert expected.name == 'Arya'