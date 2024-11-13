class Pirate:
    def __init__(self, name, job='Scallywag'):
        self.name = name
        self.job = job
        self.cursed = False
        self.heinous_count = 0
        self.booty = 0

    def is_cursed(self):
        return self.cursed

    def commit_heinous_act(self):
        self.heinous_count += 1
        if self.heinous_count >= 3:
            self.cursed = True

    def rob_ship(self):
        self.booty += 1