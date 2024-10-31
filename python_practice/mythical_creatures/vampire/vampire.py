class Vampire:
    def __init__(self, name, pet='bat'):
        self.name = name 
        self.pet = pet
        self.thirsty = True
    
    def drink(self):
        self.thirsty = False