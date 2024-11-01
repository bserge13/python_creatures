class Dragon:
    def __init__(self, name, color, rider):
        self.name = name
        self.color = color
        self.rider = rider
        self.hungry = True
        self.eat_count = 0

    def is_hungry(self):
        return self.hungry

    def eat(self):
        self.eat_count += 1
        if self.eat_count >= 3:
            self.hungry = False

    def sleep(self):
        self.eat_count = 0 
        self.hungry = True
# this function not in the original/ruby mythical creatures