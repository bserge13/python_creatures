class Medusa:
    def __init__(self, name):
        self.name = name
        self.statues = []

    def stare(self, victim):
        self.statues.append(victim)
        victim.stoned = True


class Person:
    def __init__(self, name):
        self.name = name
        self.stoned = False

    def is_stoned(self):
        return self.stoned