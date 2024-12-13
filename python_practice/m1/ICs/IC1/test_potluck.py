import pytest 
from dish import Dish
from potluck import Potluck

def test_dish_attrs():
    dish = Dish('Couscous Salad', 'appetizer')
    
    assert dish.name == 'Couscous Salad'
    assert dish.category == 'appetizer'

def test_potluck_attrs():
    potluck = Potluck('7-13-18')
    
    assert potluck.date == '7-13-18'
    assert potluck.dishes == []
    
    salad = Dish('Couscous Salad', 'appetizer')
    meatball = Dish('Cocktail Meatballs', 'entre')
    
    potluck.add_dish(salad)
    potluck.add_dish(meatball)
    
    assert potluck.dishes == [salad, meatball]
    assert len(potluck.dishes) == 2