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

        if not (self.consec_vertical(coordinates)) or not (self.consec_horizontal(coordinates)):
            return False

        # if not and empty coordinate cell:
            # return False
        return True

    def consec_vertical(self, coordinates):
        # letter = coordinates[0][1]
        # 'A'
        letters = [coord[0] for coord in coordinates]
        # ['A', 'B', 'C']
        number = int(coordinates[0][1])
        # 1
        # numbers = [int(coord[1]) for coord in coordinates]
        # [1, 2, 3]
        letters.sort()
        consec = letters == [chr(ord(letters[0]) + i) for i in range(len(letters))]

        same_column = all(coord[1] == number for coord in coordinates)
        
        return consec and same_column 
        
        # if letters != sorted(letters):
        #     return False
        # return numbers == list(range(min(numbers), max(numbers) + 1))
        # return all(coord[1] == number for coord in coordinates)

    def consec_horizontal(self, coordinates):
        row_letter = coordinates[0][0]
        # 'A'
        # letters = [coord[0] for coord in coordinates]
        # ['A', 'B', 'C']
        # number = int(coordinates[0][1])
        # 1
        numbers = [int(coord[1]) for coord in coordinates]
        # [1, 2, 3]
        # return all(numbers[i] == numbers[i-1] + 1 for i in range(1, len(numbers))) and [letter == i for i in letters]
        numbers.sort()
        consec = numbers == list(range(numbers[0], numbers[0] + len(numbers)))
        same_row = all(coord[0] == row_letter for coord in coordinates)

        return consec and same_row

    # def consec_coords(self, coordinates):
        # rows = []
        # columns = []
        # for coord in coordinates:
        #     row,column = coord[0], int(coord[1])
        #     rows.append(row)
        #     columns.append(column)
    # return rows == sorted(rows) and columns == sorted(columns) and all(columns[i] == columns[i-1] + 1 for i in range(1, len(columns)))

