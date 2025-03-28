class Friend:
    def __init__(self, name):
        self.name = name
        self.tired = False
        self.play_count = 0
        self.demenior = 'Playful'
        self.age = 1

    def play_with(self, friend):
        self.play_count += 1
        # Look to maybe make this a Loki class function()