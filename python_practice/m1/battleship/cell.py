class Cell:
    def __init__(self, coordinate):
        self.coordinate = coordinate
        self.ship = None

    def is_empty(self):
        return self.ship == None

    def place_ship(self, ship):
        self.ship = ship