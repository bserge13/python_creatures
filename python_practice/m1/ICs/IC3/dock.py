class Dock:
    def __init__(self, name, max_rental_time):
        self.name = name
        self.max_rental_time = max_rental_time
        self.rental_log = {}
    
    def rent(self, boat, renter):
        self.rental_log[boat] = renter
        boat.add_hour()
    
    def charge(self, boat):
        if boat in self.rental_log:
            card = self.rental_log[boat].credit_card_number
            if boat.hours_rented > self.max_rental_time:
                return {'card_number': card, 'amount': boat.price_per_hour * self.max_rental_time}
            else:
                return {'card_number': card, 'amount': boat.price_per_hour * boat.hours_rented}