class Loki:
    def __init__(self):
        self.name = 'Loki'
        self.breed = 'Couch Hippo'
        self.nickname = 'Little Puss'
        self.hungry = True
        self.eat_counter = 0
        self.friends = []

    def eat(self):
        self.eat_counter += 1

    def has_friends(self):
        return True if len(self.friends) > 0 else False

    def add_friend(self, friend):
        self.friends.append(friend)

    def play_with(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
        friend.play_count += 1

    def speak(self):
        if len(self.friends) == 0:
            return 'I have no friends (womp womp)'
        else:
            greeting = [f"Hi, {friend.name}!" for friend in self.friends]
            return ' '.join(greeting)

    def eat(self):
        ...