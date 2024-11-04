class Werewolf:
    def __init__(self, name, location=None):
        self.name = name
        self.location = location
        self.human = True
        self.wolf = False
        self.hungry = False
        self.victims = []

    def is_human(self):
        return self.human

    def is_wolf(self):
        return self.wolf

    def change(self):
        self.wolf = not self.wolf
        self.human = not self.human
        self.hungry = not self.hungry
    
    def is_hungry(self):
        return self.hungry

    def consume_victim(self, victim):
        self.victims.append(victim)

class Victim:
    def __init__(self):
        ...