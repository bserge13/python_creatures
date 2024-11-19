class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.health = length

    def is_sunk(self):
        return self.health == 0

    def hit(self):
        self.health -= 1