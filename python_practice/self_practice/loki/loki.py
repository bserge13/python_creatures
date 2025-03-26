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
