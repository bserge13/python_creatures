class Activity:
    def __init__(self, name):
        self.name = name
        self.participants = {}
        self.total_cost = 0
    
    def add_participant(self, participant, cost):
        self.participants[participant] = cost
        self.total_cost += cost