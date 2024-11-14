class Vehicle:
    def __init__(self, vehicle_data):
        self.vin = vehicle_data['vin']
        self.year = vehicle_data['year']
        self.make = vehicle_data['make']
        self.model = vehicle_data['model'] 
        self.engine = vehicle_data['engine'] 
        self.plate_type = None
        self.registration_date = None