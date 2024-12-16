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
    
    def menu(self):
        menu = {
            'appetizer': [],
            'entre': [],
            'dessert': []
        }
        for dish in self.dishes:
            if dish.category in menu:
                menu[dish.category].append(dish.name)
        
        for item in menu:
            menu[item].sort()
        
        return menu
        
        # categories = [set(dish.category for dish in self.dishes)]
        # menu = dict(categories)
        
        # for dish in self.dishes:
        #     ...
        # return menu