import pytest 
from registrant import Registrant

def test_registrant_class():
    reg1 = Registrant('Loki', 18, True)
    reg2 = Registrant('Karl', 15)

    assert reg1.name == 'Loki' 
    assert reg1.age == 18
    assert reg1.has_permit() == True
    assert reg1.license_data == {'written': False, 'license': False, 'renewed': False}

    assert reg2.name == 'Karl'
    assert reg2.age == 15
    assert reg2.has_permit() == False
    assert reg2.license_data == {'written': False, 'license': False, 'renewed': False}
    reg2.earn_permit() 
    assert reg2.has_permit() == True