class Ogre:
    def __init__(self, name, home='Swamp'):
        self.name = name 
        self.home = home
        self.encounter_counter = 0
        self.swings = 0

    def encounter(self, human):
        self.encounter_counter += 1
        if self.encounter_counter % 3 == 0:
            human.notice_ogre = True
            self.swings += 1
        else:
            human.notice_ogre = False

    def swing_at(self, victim):
        self.swings += 1


class Human:
    def __init__(self, name='Jane'):
        self.name = name
        self.notice_ogre = False