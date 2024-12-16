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
    meatballs = Dish('Cocktail Meatballs', 'entre')
    
    potluck.add_dish(salad)
    potluck.add_dish(meatballs)
    
    assert potluck.dishes == [salad, meatballs]
    assert len(potluck.dishes) == 2

def test_iteration_3():
    potluck = Potluck('7-13-18')
    
    salad = Dish('Couscous Salad', 'appetizer')
    pizza = Dish('Summer Pizza', 'appetizer')
    pork = Dish('Roast Pork', 'entre')
    meatballs = Dish('Cocktail Meatballs', 'entre')
    candy = Dish('Candy Salad', 'dessert')

    potluck.add_dish(salad)
    potluck.add_dish(pizza)
    potluck.add_dish(pork)
    potluck.add_dish(meatballs)
    potluck.add_dish(candy)

    assert potluck.get_all_from_category('appetizer') == [salad, pizza]
    assert potluck.get_all_from_category('appetizer')[0] == salad
    assert potluck.get_all_from_category('appetizer')[0].name == salad.name

def test_iteration_4():
    potluck = Potluck('7-13-18')
    
    salad = Dish('Couscous Salad', 'appetizer')
    pizza = Dish('Summer Pizza', 'appetizer')
    pork = Dish('Roast Pork', 'entre')
    meatballs = Dish('Cocktail Meatballs', 'entre')
    candy = Dish('Candy Salad', 'dessert')
    dip = Dish('Bean Dip', 'appetizer')

    potluck.add_dish(salad)
    potluck.add_dish(pizza)
    potluck.add_dish(pork)
    potluck.add_dish(meatballs)
    potluck.add_dish(candy)
    potluck.add_dish(dip)

    assert potluck.menu() == {'appetizer': [dip.name, salad.name, pizza.name], 
                            'entre': [meatballs.name, pork.name],
                            'dessert': [candy.name]
                            }
    assert potluck.ratio('appetizer') == 50.0