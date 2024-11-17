import requests

class DmvDataServices:
    def load_data(self, source):
        return requests.get(source)

    def wa_ev_registration(self):
        response = self.load_data('https://data.wa.gov/resource/rpr4-cgyd.json')
        return response.json()

    def co_dmv_office_locations(self):
        response = self.load_data('https://data.colorado.gov/resource/dsw3-mrn4.json')
        return response.json()

    def ny_dmv_office_locations(self):
        response = self.load_data('https://data.ny.gov/resource/9upz-c7xg.json')
        return response.json()

    def mo_dmv_office_locations(self):
        response = self.load_data('https://data.mo.gov/resource/835g-7keg.json') 
        return response.json()