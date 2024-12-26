class Dock:
    def __init__(self, name, max_rental_time):
        self.name = name
        self.max_rental_time = max_rental_time
        self.rental_log = {}
    
    def rent(self, boat, renter):
        if boat not in self.rental_log:
            self.rental_log[boat] = {'renter': renter, 'rented': True}
            boat.add_hour()
        else: 
            self.rental_log[boat]['rented'] = True
            boat.add_hour()
    
    def charge(self, boat):
        if boat in self.rental_log:
            card = self.rental_log[boat]['renter'].credit_card_number
            if boat.hours_rented > self.max_rental_time:
                return {'card_number': card, 'amount': boat.price_per_hour * self.max_rental_time}
            else:
                return {'card_number': card, 'amount': boat.price_per_hour * boat.hours_rented}
    
    def return_boat(self, boat):
        if boat in self.rental_log:
            self.rental_log[boat]['rented'] = False
    
    def log_hour(self):
        for boat, status in self.rental_log.items():
            if status['rented'] == True:
                boat.hours_rented += 1
    """
    .items() turns the dict key/value pairs into 
    a list which is iterable and transformable vs 
    an imutable tupple
    """
    
    def revenue(self):
        total = 0
        for boat, status in self.rental_log.items():
            if status['rented'] == False:
                if boat.hours_rented > self.max_rental_time:
                    total += boat.price_per_hour * self.max_rental_time
                else:
                    total += boat.price_per_hour * boat.hours_rented
        return total