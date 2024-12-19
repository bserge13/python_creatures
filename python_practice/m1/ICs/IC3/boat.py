class Boat:
    def __init__(self, type, price_per_hour):
        self.type = type
        self.price_per_hour = price_per_hour
        self.hours_rented = 0
    
    def add_hour(self):
        self.hours_rented += 1