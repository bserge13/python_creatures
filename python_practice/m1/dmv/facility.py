class Facility:
    def __init__(self, facility_data):
        self.name = facility_data['name']
        self.address = facility_data['address']
        self.phone = facility_data['phone']
        self.services = []
        self.registered_vehicles = []
        self.collected_fees = 0

    def add_service(self, service):
        self.services.append(service)
