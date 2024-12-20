class Dock:
    def __init__(self, name, max_rental_time):
        self.name = name
        self.max_rental_time = max_rental_time
        self.rental_log = {}
    
    def rent(self, boat, renter):
        self.rental_log[boat] = renter