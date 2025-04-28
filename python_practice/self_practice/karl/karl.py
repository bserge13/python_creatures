class Karl:
    def __init__(self):
        self.name = 'Karl'
        self.nickname = 'Big Puss'
        self.tired = False
        self.hungry = True 
        self.treat_counter = 0
    
    def meow(self):
        self.treat_counter += 1
        if self.treat_counter >= 3:
            self.tired = True 
            self.hungry = False
    
    def speak(self, name=None):
        if name == None:
            return 'I am Karl, hear me ROAR!'
        else:
            return f"I am Karl, hear me ROAR, {name}!"