from cell import Cell

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

        for coord in coordinates:
            if not self.valid_coordinate(coord):
                return False

        if not (self.consec_vertical(coordinates)) or not self.consec_horizontal(coordinates):
            return False

        return True

    def consec_vertical(self, coordinates):
        rows = [coord[0] for coord in coordinates]
        columns = [int(coord[1]) for coord in coordinates]

        if len(set(columns)) != 1:
            return False
        return rows == [chr(ord(rows[0]) + i) for i in range(len(rows))]

        # for coord in coordinates:
        #     if coord[0] != letter:
        #         return False
        #     else:
        #         return True

    def consec_horizontal(self, coordinates):
        number = int(coordinates[0][1])

        for coord in coordinates:
            if int(coord[1]) != number:
                return False
            else:
                return True


    # def consec_coords(self, coordinates):
        # rows = []
        # columns = []
        # for coord in coordinates:
        #     row,column = coord[0], int(coord[1])
        #     rows.append(row)
        #     columns.append(column)
    # return rows == sorted(rows) and columns == sorted(columns) and all(columns[i] == columns[i-1] + 1 for i in range(1, len(columns)))
