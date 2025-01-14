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
            activity_dues = activity.owed()
            for participant, amount in activity_dues.items():
                if participant in reunion_bill:
                    reunion_bill[participant] += amount
                else:
                    reunion_bill[participant] = amount
        return reunion_bill
    
    def print_bill(self):
        bill = ""
        for participant,owed in self.split_bill().items():
            bill += f"{participant} owes ${owed}\n"
        return bill.strip()