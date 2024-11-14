import pytest 
from facility import Facility
from vehicle import Vehicle

def test_facility_attrs():
    facility1 = Facility({'name': 'DMV Tremont Branch', 'address': '2855 Tremont Place Suite 118 Denver CO 80205', 'phone': '(720) 865-4600'})
    facility2 = Facility({'name': 'DMV Northeast Branch', 'address': '4685 Peoria Street Suite 101 Denver CO 80239', 'phone': '(720) 865-4600'})

    assert facility1.address == '2855 Tremont Place Suite 118 Denver CO 80205'
    assert facility1.name == 'DMV Tremont Branch'
    assert facility1.phone == '(720) 865-4600'
    assert facility1.services == []

    assert facility2.address == '4685 Peoria Street Suite 101 Denver CO 80239'
    assert facility2.name == 'DMV Northeast Branch'
    assert facility2.phone == '(720) 865-4600'
    assert facility2.services == []
