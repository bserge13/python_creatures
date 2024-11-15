import datetime

class Vehicle:
    def __init__(self, vehicle_data):
        self.vin = vehicle_data['vin']
        self.year = vehicle_data['year']
        self.make = vehicle_data['make']
        self.model = vehicle_data['model'] 
        self.engine = vehicle_data['engine'] 
        self.plate_type = None
        self.registration_date = None

    def is_antique(self):
        return datetime.date.today().year - self.year >= 25

    def is_electric(self):
        return self.engine == ':ev'

    def register(self):
        self.registration_date = datetime.date.today()
        if self.is_antique():
            self.plate_type = ':antique'
        elif self.is_electric():
            self.plate_type = ':ev'
        else:
            self.plate_type = ':regular'