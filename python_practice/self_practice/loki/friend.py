class Friend:
    def __init__(self, name):
        self.name = name
        self.tired = False
        self.play_count = 0
        self.age = 1

    def play_with(self, friend):
        if self in friend.friends:
            self.play_count += 1
        return 'not friends'

    def demenior(self):
        if self.play_count >= 3:
            return 'Tired'
        return 'Playful'