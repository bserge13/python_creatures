import pytest
from dmv_data_services import DmvDataServices 
from vehicle_factory import VehicleFactory 
from vehicle import Vehicle

def test_create_vehicles():
    factory = VehicleFactory()
    dmv = DmvDataServices()
    wa_reg = factory.create_vehicles(dmv.wa_ev_registration())

    assert isinstance(wa_reg, list)
    assert len(wa_reg) > 0

    first_wa = wa_reg[0]
    assert isinstance(first_wa, Vehicle)

    assert hasattr(first_wa, 'vin')
    assert hasattr(first_wa, 'year')
    assert hasattr(first_wa, 'make')
    assert hasattr(first_wa, 'model')
    assert hasattr(first_wa, 'engine')