class Medusa:
    def __init__(self, name):
        self.name = name
        self.statues = []

    def stare(self, victim):
        self.statues.append(victim)
        victim.stoned = True
        if len(self.statues) == 4:
            first = self.statues.pop(0)
            first.stoned = False


class Person:
    def __init__(self, name):
        self.name = name
        self.stoned = False

    def is_stoned(self):
        return self.stoned