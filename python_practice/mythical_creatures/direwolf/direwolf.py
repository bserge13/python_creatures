class Direwolf:
    def __init__(self, name, home='Beyond the Wall', size='Massive'):
        self.name = name
        self.home = home
        self.size = size
        self.starks = []
        self.hunts = True

    def starks_to_protect(self):
        return self.starks

    def protect(self, stark):
        if self.home == stark.location and len(self.starks) < 2:
            self.starks.append(stark)
            stark.safe = True
            self.hunts = False

    def hunts_walkers(self):
        return self.hunts

    def leave(self, stark):
        self.starks.remove(stark)
        stark.safe = False
        if len(self.starks) == 0:
            self.hunts = True
        return stark

class Stark:
    def __init__(self, name, location='Winterfell'):
        self.name = name 
        self.location = location
        self.house_words = 'Winter is coming'
        self.safe = False

    def is_safe(self):
        return self.safe