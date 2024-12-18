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

    def register_vehicle(self, vehicle):
        if 'Vehicle Registration' in self.services:
            self.registered_vehicles.append(vehicle)
            vehicle.register()
            if vehicle.is_antique():
                self.collected_fees += 25
            elif vehicle.is_electric():
                self.collected_fees += 200
            else:
                self.collected_fees += 100

    def administer_written_test(self, registrant):
        if 'Written Test' in self.services and registrant.permit == True and registrant.age >= 16:
            registrant.take_written()

    def administer_road_test(self, registrant):
        if 'Road Test' in self.services and registrant.license_data['written'] == True:
            registrant.take_road_test()

    def renew_drivers_license(self, registrant):
        if 'Renew License' in self.services and registrant.license_data['license'] == True:
            registrant.renew_license()