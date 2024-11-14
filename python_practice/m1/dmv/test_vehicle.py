import pytest 
from vehicle import Vehicle

def test_vehicle_attrs():
    cruz = Vehicle({'vin': '123456789abcdefgh', 'year': 2012, 'make': 'Chevrolet', 'model': 'Cruz', 'engine': ':ice'})
    bolt = Vehicle({'vin': '987654321abcdefgh', 'year': 2019, 'make': 'Chevrolet', 'model': 'Bolt', 'engine': ':ev'})

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
