import pytest 
import datetime
from facility import Facility
from vehicle import Vehicle

facility1 = Facility({'name': 'DMV Tremont Branch', 'address': '2855 Tremont Place Suite 118 Denver CO 80205', 'phone': '(720) 865-4600'})
facility2 = Facility({'name': 'DMV Northeast Branch', 'address': '4685 Peoria Street Suite 101 Denver CO 80239', 'phone': '(720) 865-4600'})

def test_facility_attrs():
    assert facility1.address == '2855 Tremont Place Suite 118 Denver CO 80205'
    assert facility1.name == 'DMV Tremont Branch'
    assert facility1.phone == '(720) 865-4600'

    assert facility2.address == '4685 Peoria Street Suite 101 Denver CO 80239'
    assert facility2.name == 'DMV Northeast Branch'
    assert facility2.phone == '(720) 865-4600'

def test_class_functions():
    cruz = Vehicle({'vin': '123456789abcdefgh', 'year': 2012, 'make': 'Chevrolet', 'model': 'Cruz', 'engine': ':ice'})
    camaro = Vehicle({'vin': '1a2b3c4d5e6f', 'year': 1969, 'make': 'Chevrolet', 'model': 'Camaro', 'engine': ':ice'})
    bolt = Vehicle({'vin': '987654321abcdefgh', 'year': 2019, 'make': 'Chevrolet', 'model': 'Bolt', 'engine': ':ev'})

    facility1.add_service('Vehicle Registration') 
    assert facility1.services == ["Vehicle Registration"]

    assert facility1.registered_vehicles == []
    assert facility1.collected_fees == 0

    facility1.register_vehicle(cruz)
    assert cruz.registration_date == datetime.date.today()
    assert cruz.plate_type == ':regular'
    assert facility1.registered_vehicles == [cruz]
    assert facility1.collected_fees == 100

    facility1.register_vehicle(camaro)
    assert camaro.registration_date == datetime.date.today()
    assert camaro.plate_type == ':antique'
    assert facility1.registered_vehicles == [cruz, camaro]

    facility1.register_vehicle(bolt)
    assert bolt.registration_date == datetime.date.today()
    assert bolt.plate_type == ':ev'
    assert facility1.registered_vehicles == [cruz, camaro, bolt]
    assert facility1.collected_fees == 325

    assert facility2.registered_vehicles == []
    facility2.register_vehicle(bolt)
    assert facility2.registered_vehicles == []
    assert facility2.collected_fees == 0

