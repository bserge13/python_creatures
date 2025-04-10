class Friend:
    def __init__(self, name):
        self.name = name
        self.tired = False
        self.play_count = 0
        self.age = 1

    def play_with(self, friend):
        if self in friend.friends:
            self.play_count += 1
            if self.play_count >= 3:
                self.age += 1
        return "We're not friends"

    def demenior(self):
        if self.play_count >= 3:
            self.tired = True
            return 'Tired'
        return 'Playful'