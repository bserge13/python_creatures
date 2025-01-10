class Reunion:
    def __init__(self, name):
        self.name = name
        self.activities = []
    
    def add_activity(self, activity):
        self.activities.append(activity)