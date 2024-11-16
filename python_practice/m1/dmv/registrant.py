class Registrant:
    def __init__(self, name, age, permit=False):
        self.name = name
        self.age = age
        self.permit = permit
        self.license_data = {'written': False, 'license': False, 'renewed': False}

    def has_permit(self):
        return self.permit

    def earn_permit(self):
        self.permit = True

    def take_written(self):
        self.license_data['written'] = True

    def take_road_test(self):
        self.license_data['license'] = True