import pytest 
from potluck import Dish

def test_attrs():
    dish = Dish('Couscous Salad', 'appetizer')
    
    assert dish.name == 'Couscous Salad'
    assert dish.category == 'appetizer'