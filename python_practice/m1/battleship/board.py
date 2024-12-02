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

        if not self.consec_coords(coordinates):
            return False

        # if not and empty coordinate cell:
            # return False
        return True

    def consec_coords(self, coordinates):
        coord_letters = [coord[0] for coord in coordinates]
        coord_nums = [int(coord[1]) for coord in coordinates]
        # horizontal = all(coord_letters[0] == coord for coord in coord_letters) and sorted(coord_nums) == list(range(min(coord_nums), max(coord_nums) + 1))
        horizontal = all(coord_letters[0] == coord for coord in coord_letters) and coord_nums == list(range(min(coord_nums), min(coord_nums) + len(coord_nums)))
        # vertical = all(coord_nums[0] == num for num in coord_nums) and sorted(coord_letters) == [chr(ord(coord_letters[0]) + i) for i in range(len(coord_letters))]
        vertical = all(coord_nums[0] == num for num in coord_nums) and coord_letters == [chr(ord(coord_letters[0]) + i) for i in range(len(coord_letters))]

        return horizontal or vertical and not self.diagonal(coord_letters, coord_nums)
        # return coord_letters == sorted(coord_letters) and coord_nums == sorted(coord_nums) and all(coord_nums[i] == coord_nums[i-1] + 1 for i in range(1, len(coord_nums))) and not self.diagonal(coord_letters, coord_nums)

    def diagonal(self, coord_letters, coord_nums):
        # if coord_letters[0] != coord_letters[1]:
        #     if coord_nums[1] == coord_nums[0] + 1:
        #         return True
        # return False
        return sorted(coord_letters) == [chr(ord(coord_letters[0]) + i) for i in range(len(coord_letters))] and sorted(coord_nums) == list(range(min(coord_nums), max(coord_nums) + 1))
