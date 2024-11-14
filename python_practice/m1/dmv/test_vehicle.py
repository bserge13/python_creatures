import pytest 
from vehicle import Vehicle

def test_vehicle_attrs():
    cruz = Vehicle({'vin': '123456789abcdefgh', 'year': 2012, 'make': 'Chevrolet', 'model': 'Cruz', 'engine': ':ice'})
    bolt = Vehicle({'vin': '987654321abcdefgh', 'year': 2019, 'make': 'Chevrolet', 'model': 'Bolt', 'engine': ':ev'})
    # camaro = Vehicle({'vin': '1a2b3c4d5e6f', 'year': 1969, 'make': 'Chevrolet', 'model': 'Camaro', 'engine': ':ice'})
    assert cruz.vin == '123456789abcdefgh'
    assert cruz.year == 2012
    assert cruz.make == 'Chevrolet'
    assert cruz.model == 'Cruz'
    assert cruz.engine == ':ice'

    assert bolt.vin == '987654321abcdefgh'
    assert bolt.year == 2019
    assert bolt.make == 'Chevrolet'
    assert bolt.model == 'Bolt'
    assert bolt.engine == ':ev'