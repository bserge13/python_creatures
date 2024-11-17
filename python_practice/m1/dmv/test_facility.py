import pytest 
import datetime
from facility import Facility
from vehicle import Vehicle
from registrant import Registrant

facility1 = Facility({'name': 'DMV Tremont Branch', 'address': '2855 Tremont Place Suite 118 Denver CO 80205', 'phone': '(720) 865-4600'})
facility2 = Facility({'name': 'DMV Northeast Branch', 'address': '4685 Peoria Street Suite 101 Denver CO 80239', 'phone': '(720) 865-4600'})

cruz = Vehicle({'vin': '123456789abcdefgh', 'year': 2012, 'make': 'Chevrolet', 'model': 'Cruz', 'engine': ':ice'})
camaro = Vehicle({'vin': '1a2b3c4d5e6f', 'year': 1969, 'make': 'Chevrolet', 'model': 'Camaro', 'engine': ':ice'})
bolt = Vehicle({'vin': '987654321abcdefgh', 'year': 2019, 'make': 'Chevrolet', 'model': 'Bolt', 'engine': ':ev'})

registrant1 = Registrant('Nova', 18, True)
registrant2 = Registrant('Loki', 16)
registrant3 = Registrant('Karl', 15)

def test_facility_attrs():
    assert facility1.address == '2855 Tremont Place Suite 118 Denver CO 80205'
    assert facility1.name == 'DMV Tremont Branch'
    assert facility1.phone == '(720) 865-4600'

    assert facility2.address == '4685 Peoria Street Suite 101 Denver CO 80239'
    assert facility2.name == 'DMV Northeast Branch'
    assert facility2.phone == '(720) 865-4600'

def test_class_functions():
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

def test_written_test():
    assert registrant1.license_data == {'written': False, 'license': False, 'renewed': False}
    assert registrant1.has_permit() == True
    facility1.administer_written_test(registrant1)
    assert registrant1.license_data == {'written': False, 'license': False, 'renewed': False}
    facility1.add_service('Written Test')
    facility1.administer_written_test(registrant1)
    assert registrant1.license_data == {'written': True, 'license': False, 'renewed': False}

    assert registrant2.age == 16
    assert registrant2.has_permit() == False
    facility1.administer_written_test(registrant2)
    registrant2.earn_permit()
    facility1.administer_written_test(registrant2)
    assert registrant2.license_data == {'written': True, 'license': False, 'renewed': False}

    assert registrant3.age == 15
    assert registrant3.has_permit() == False
    facility1.administer_written_test(registrant3)
    registrant3.earn_permit()
    facility1.administer_written_test(registrant3)
    assert registrant3.license_data == {'written': False, 'license': False, 'renewed': False}

def test_road_test():
    facility1.administer_road_test(registrant3)
    registrant3.earn_permit()
    facility1.administer_road_test(registrant3)
    assert registrant3.license_data == {'written': False, 'license': False, 'renewed': False}

    assert registrant1.license_data == {'written': True, 'license': False, 'renewed': False}
    facility1.services == []

    facility1.add_service('Written Test')
    facility1.add_service('Road Test')
    facility1.services == ['Written Test', 'Road Test']
    facility1.administer_road_test(registrant1)
    assert registrant1.license_data == {'written': True, 'license': True, 'renewed': False}
    facility1.administer_road_test(registrant2)
    assert registrant2.license_data == {'written': True, 'license': True, 'renewed': False}

def test_renew_license():
    facility1.renew_drivers_license(registrant1)
    assert registrant1.license_data == {'written': True, 'license': True, 'renewed': False}
    facility1.add_service('Written Test')
    facility1.add_service('Road Test')
    facility1.add_service('Renew License')
    facility1.services == ['Written Test', 'Road Test', 'Renew License']
    facility1.renew_drivers_license(registrant1)
    assert registrant1.license_data == {'written': True, 'license': True, 'renewed': True}

    facility1.renew_drivers_license(registrant3)
    assert registrant3.license_data == {'written': False, 'license': False, 'renewed': False}

    facility1.renew_drivers_license(registrant2)
    assert registrant2.license_data == {'written': True, 'license': True, 'renewed': True}
