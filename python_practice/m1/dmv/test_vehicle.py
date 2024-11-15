import pytest 
from vehicle import Vehicle
import datetime

cruz = Vehicle({'vin': '123456789abcdefgh', 'year': 2012, 'make': 'Chevrolet', 'model': 'Cruz', 'engine': ':ice'})
camaro = Vehicle({'vin': '1a2b3c4d5e6f', 'year': 1969, 'make': 'Chevrolet', 'model': 'Camaro', 'engine': ':ice'})
bolt = Vehicle({'vin': '987654321abcdefgh', 'year': 2019, 'make': 'Chevrolet', 'model': 'Bolt', 'engine': ':ev'})

def test_vehicle_attrs():
    assert cruz.vin == '123456789abcdefgh'
    assert cruz.year == 2012
    assert cruz.make == 'Chevrolet'
    assert cruz.model == 'Cruz'
    assert cruz.engine == ':ice'
    assert cruz.plate_type == None
    assert cruz.registration_date == None

    assert bolt.vin == '987654321abcdefgh'
    assert bolt.year == 2019
    assert bolt.make == 'Chevrolet'
    assert bolt.model == 'Bolt'
    assert bolt.engine == ':ev'
    assert bolt.plate_type == None
    assert bolt.registration_date == None

def test_class_functions():
    mustang = Vehicle({'vin': '123456789abcljfce', 'year': 2014, 'make': 'Ford', 'model': 'Mustang', 'engine': ':regular'})

    assert camaro.is_antique() == True
    assert bolt.is_antique() == False
    assert cruz.is_antique() == False

    assert camaro.is_electric() == False
    assert bolt.is_electric() == True
    assert cruz.is_electric() == False

    assert mustang.registration_date == None
    mustang.register()
    assert mustang.registration_date == datetime.date.today()