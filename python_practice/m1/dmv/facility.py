class Facility:
    def __init__(self, facility_data):
        self.name = facility_data['name']
        self.address = facility_data['address']
        self.phone = facility_data['phone']
        self.services = []