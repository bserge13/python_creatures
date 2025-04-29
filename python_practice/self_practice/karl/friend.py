class Friend:
    def __init__(self, name=None):
        self.name = name
    
    def play_with(self, friend):
        return f"Let's play, {friend.nickname}!"