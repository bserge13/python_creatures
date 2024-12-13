class Potluck:
    def __init__(self, date):
        self.date = date
        self.dishes = []
    
    def add_dish(self, dish):
        self.dishes.append(dish)