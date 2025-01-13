class Reunion:
    def __init__(self, name):
        self.name = name
        self.activities = []
    
    def add_activity(self, activity):
        self.activities.append(activity)
    
    def event_cost(self):
        cost = 0
        for activity in self.activities:
            cost += activity.total_cost
        return cost
    
    def split_bill(self):
        reunion_bill = {}
        for activity in self.activities:
            for participant, money in activity.participants.items():
                if participant not in reunion_bill:
                    reunion_bill[participant]
        return reunion_bill 