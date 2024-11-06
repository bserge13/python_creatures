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
            if self.swings >= 2:
                human.is_hit = True 
        else:
            human.notice_ogre = False

    def swing_at(self, victim):
        self.swings += 1

    def apologize(self, victim):
        self.encounter_counter = 0
        self.swings = 0
        victim.is_hit = False
        victim.notice_ogre = False


class Human:
    def __init__(self, name='Jane'):
        self.name = name
        self.notice_ogre = False
        self.is_hit = False