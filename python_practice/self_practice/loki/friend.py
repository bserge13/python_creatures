class Friend:
    def __init__(self, name):
        self.name = name
        self.tired = False
        self.play_count = 0
        self.age = 1

    def play_with(self, friend):
        self.play_count += 1

    def demenior(self):
        if self.play_count >= 3:
            return 'Tired'
        return 'Playful'