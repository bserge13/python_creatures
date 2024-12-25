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
            renter = self.rental_log[boat]
            card = renter.credit_card_number          
            return {'card_number': card,
                    'amount': boat.price_per_hour * boat.hours_rented}
    # if hours exceed docks max_rental_time, the extra hours are not counted/charged