class Registrant:
    def __init__(self, name, age, permit=False):
        self.name = name
        self.age = age
        self.permit = permit
        self.license_data = {'written': False, 'license': False, 'renewed': False}
        