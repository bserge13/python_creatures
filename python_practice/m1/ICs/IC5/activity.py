class Activity:
    def __init__(self, name):
        self.name = name
        self.participants = {}
        self.total_cost = 0
    
    def add_participant(self, participant, cost):
        self.participants[participant] = cost
        self.total_cost += cost
    
    def split(self):
        return self.total_cost / len(self.participants)
    
    def owed(self):
        owed = {}
        for participant,money in self.participants.items():
            value = self.split() - money
            owed[participant] = round(value, 2)
        return owed