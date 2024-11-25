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
        return coordinate in self.cells and not self.cells[coordinate].is_fired_upon()

    def valid_placement(self, ship, coordinates):
        if len(coordinates) != ship.length:
            return False
        if not self.consec_coords(coordinates):
            return False
        for coord in coordinates:
            if not self.valid_coordinate(coord):
                return False
        return True

    def consec_coords(self, coordinates):
        rows = []
        columns = []
        for coord in coordinates:
            row,column = coord[0], int(coord[1])
            rows.append(row)
            columns.append(column)
        return rows == sorted(rows) and columns == sorted(columns) and all(columns[i] == columns[i-1] + 1 for i in range(1, len(columns)))

    # def consec_horizontal(self, coordinates):
    #     return 

    # def consec_vertical(self, coordinates):
    #     return 
