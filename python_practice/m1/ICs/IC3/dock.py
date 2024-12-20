class Dock:
    def __init__(self, name, max_rental_time):
        self.name = name
        self.max_rental_time = max_rental_time
        self.rental_log = {}
    
    def rent(self, boat, renter):
        self.rental_log[boat] = renter
    
    def charge(self, boat):
        return {'card_number': 'renter_card_num',
                'amount': 'boat pp_hr * hrs_rented'}
    # if hours exceed docks max_rental_time, the extra hours are not counted/charged