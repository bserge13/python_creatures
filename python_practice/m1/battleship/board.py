from cell import Cell
from ship import Ship

class Board:
    def __init__(self):
        self.cells = {
            'A1': Cell('A1'),
            'A2': Cell('A2'),
            'A3': Cell('A3'),
            'A4': Cell('A4'),
            'B1': Cell('B1'),
            'B2': Cell('B2'),
            'B3': Cell('B3'),
            'B4': Cell('B4'),
            'C1': Cell('C1'),
            'C2': Cell('C2'),
            'C3': Cell('C3'),
            'C4': Cell('C4'),
            'D1': Cell('D1'),
            'D2': Cell('D2'),
            'D3': Cell('D3'),
            'D4': Cell('D4'),
        }

    def valid_coordinate(self, coordinate):
        return coordinate in self.cells and self.cells[coordinate].is_fired_upon() == False

    def valid_placement(self, ship, coordinates):
        return len(coordinates) == ship.length and self.consec_horizontal(coordinates) and self.consec_vertical(coordinates)

    def consec_horizontal(self, coordinates):
        # row = [int(coord[1]) for coord in coordinates]
        # return row
        ...

    def consec_vertical(self, coordinates):
        ...