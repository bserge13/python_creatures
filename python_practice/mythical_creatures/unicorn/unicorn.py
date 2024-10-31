class Unicorn:
    def __init__(self, name, color='silver'):
        self.name = name
        self.color = color
    
    def is_silver(self):
        return self.color == 'silver'

    def say(self, ui):
        return f"**;* {ui}! **;*"