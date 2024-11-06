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