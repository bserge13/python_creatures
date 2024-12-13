class Potluck:
    def __init__(self, date):
        self.date = date
        self.dishes = []
    
    def add_dish(self, dish):
        self.dishes.append(dish)
    
    def get_all_from_category(self, category):
        category_dishes = []
        for dish in self.dishes:
            if dish.category == category:
                category_dishes.append(dish)
        return category_dishes