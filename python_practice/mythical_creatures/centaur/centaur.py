class Centaur:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.cranky = False
        self.standing = True
        self.laying = False
        self.activity_count = 0

    def shoot(self):
        self.activity_count += 1
        if self.activity_count >= 3:
            return 'NO!'
        else:
            return 'Twang!!!'

    def run(self):
        self.activity_count += 1
        return 'Clop clop clop clop!'

    def is_cranky(self):
        if self.activity_count >= 3:
            self.cranky = True
        return self.cranky

    def is_standing(self):
        return self.standing

    def sleep(self):
        if self.standing:
            return 'NO!'

    def is_laying(self):
        return self.laying

    def lay_down(self):
        self.laying = True
        self.standing = False