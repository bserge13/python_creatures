class Ogre:
    def __init__(self, name, home='Swamp'):
        self.name = name 
        self.home = home
        self.encounter_counter = 0

    def encounter(self, human):
        self.encounter_counter += 1



class Human:
    def __init__(self, name='Jane'):
        self.name = name