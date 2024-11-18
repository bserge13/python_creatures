import pytest 
from dmv_data_services import DmvDataServices
from facility_factory import Facilityfactory
from facility import Facility

dmv = DmvDataServices()
factory = Facilityfactory()
ny_facility = factory.create_facilities(dmv.ny_dmv_office_locations())
co_facility = factory.create_facilities(dmv.co_dmv_office_locations())
mo_facility = factory.create_facilities(dmv.mo_dmv_office_locations())

def test_create_ny_facilities():
    assert isinstance(ny_facility, list)
    assert len(ny_facility) > 0

    first_ny = ny_facility[0]
    assert isinstance(first_ny, Facility)

    assert hasattr(first_ny, 'name')
    assert hasattr(first_ny, 'address')
    assert hasattr(first_ny, 'phone')
    assert hasattr(first_ny, 'services')
    assert hasattr(first_ny, 'registered_vehicles')
    assert hasattr(first_ny, 'collected_fees')

def test_create_co_facilities():
    assert isinstance(co_facility, list)
    assert len(co_facility) > 0

    first_co = co_facility[0]
    assert isinstance(first_co, Facility)

    assert hasattr(first_co, 'name')
    assert hasattr(first_co, 'address')
    assert hasattr(first_co, 'phone')
    assert hasattr(first_co, 'services')
    assert hasattr(first_co, 'registered_vehicles')
    assert hasattr(first_co, 'collected_fees')

def test_create_mo_facilities():
    assert isinstance(mo_facility, list)
    assert len(mo_facility) > 0

    first_mo = mo_facility[0]
    assert isinstance(first_mo, Facility)

    assert hasattr(first_mo, 'name')
    assert hasattr(first_mo, 'address')
    assert hasattr(first_mo, 'phone')
    assert hasattr(first_mo, 'services')
    assert hasattr(first_mo, 'registered_vehicles')
    assert hasattr(first_mo, 'collected_fees')