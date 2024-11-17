import pytest 
from dmv_data_services import DmvDataServices

def test_api_services():
    dmv = DmvDataServices()
    wa_services = dmv.wa_ev_registration()
    co_services = dmv.co_dmv_office_locations()
    ny_services = dmv.ny_dmv_office_locations()
    mo_services = dmv.mo_dmv_office_locations()

    assert isinstance(wa_services, list)
    first = wa_services[0]
    assert isinstance(first, dict)

    assert isinstance(co_services, list)
    first = co_services[0]
    assert isinstance(first, dict)

    assert isinstance(ny_services, list)
    first = ny_services[0]
    assert isinstance(first, dict)

    assert isinstance(mo_services, list)
    first = mo_services[0]
    assert isinstance(first, dict)