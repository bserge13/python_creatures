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