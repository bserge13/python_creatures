class Cell:
    def __init__(self, coordinate):
        self.coordinate = coordinate
        self.ship = None
        self.fired_upon = False

    def is_empty(self):
        return self.ship == None

    def place_ship(self, ship):
        self.ship = ship

    def is_fired_upon(self):
        return self.fired_upon

    def fire_upon(self):
        self.fired_upon = True
        if self.ship != None:
            self.ship.hit()

    def render(self, show_cell=False):
        if not self.fired_upon:
            if self.ship and show_cell:
                return 'S'
            return '.'
        
        if self.ship:
            if self.ship.is_sunk():
                return 'X'
            return 'H'
        
        return 'M'