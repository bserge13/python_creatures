import requests

class DmvDataServices:
    def load_data(self, source):
        return requests.get(source)

    def wa_ev_registration(self):
        response = self.load_data('https://data.wa.gov/resource/rpr4-cgyd.json')
        return response.json()