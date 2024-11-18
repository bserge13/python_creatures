from facility import Facility

class Facilityfactory:
    def create_facilities(self, location):
        new_facilities = []
        for office in location:
            if office['state'] == 'NY':
                details = {
                    'name': office['office_name'],
                    'address': office['street_address_line_1'],
                    'phone': office.get('public_phone_number', None),
                }
                new_facilities.append(Facility(details))
            elif office['state'] == 'CO':
                details = {
                    'name': office['dmv_office'],
                    'address': office['address_li'],
                    'phone': office['phone'],
                }
                new_facilities.append(Facility(details))
            elif office['state'] == 'MO':
                details = {
                    'name': office['name'],
                    'address': office['address1'],
                    'phone': office['phone'],
                }
                new_facilities.append(Facility(details))
        return new_facilities