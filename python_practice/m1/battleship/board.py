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
        # return len(coordinates) == ship.length and self.consec_horizontal(coordinates) and self.consec_vertical(coordinates)
        if len(coordinates) == ship.length:
            rows = []
            columns = []
            for coord in coordinates:
                row,column = coord[0], int(coord[1:])
                rows.append(row)
                columns.append(column)
            return rows == sorted(rows) and columns == sorted(columns) and all(columns[i] == columns[i-1] + 1 for i in range(1, len(columns)))
        else:
            return False

    # def consec_horizontal(self, coordinates):
    #     coords = []
    #     for coord in coordinates:
    #         column,row = coord[0], coord[1:]
    #         coords.append(row)
    #     if coords == sorted(row):
    #         return True
    #     else:
    #         return False

    # def consec_vertical(self, coordinates):
    #     coords = []
    #     for coord in coordinates:
    #         column,row = coord[0], coord[1:]
    #         coords.append(column)
    #     if coords == sorted(coords):
    #         return True
    #     else:
    #         return False