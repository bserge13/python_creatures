from vehicle import Vehicle 

class VehicleFactory:
    def create_vehicles(self, service):
        vehicles = []
        for vehicle in service:
            vehicle_data = {
                'vin': vehicle['vin_1_10'],
                'year': vehicle['model_year'],
                'make': vehicle['make'],
                'model': vehicle['model'],
                'engine': ':ev'
            }
            vehicles.append(Vehicle(vehicle_data))
        return vehicles