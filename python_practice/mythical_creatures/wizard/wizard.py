class Wizard:
    def __init__(self, name, beard=True):
        self.name = name 
        self.bearded = beard
        self.rested = True
        self.spell_count = 0
    
    def is_bearded(self):
        return self.bearded

    def incantation(self, spell):
        return f"sudo {spell}"

    def is_rested(self):
        return self.rested

    def cast(self):
        self.spell_count += 1
        if self.spell_count >= 3:
            self.rested = False
        return 'MAGIC MISSILE!'