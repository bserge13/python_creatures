class Ogre:
    def __init__(self, name, home='Swamp'):
        self.name = name 
        self.home = home
        self.encounter_counter = 0

    def encounter(self, human):
        self.encounter_counter += 1
        if self.encounter_counter >= 3:
            human.notice_ogre = True



class Human:
    def __init__(self, name='Jane'):
        self.name = name
        self.notice_ogre = False