import pytest 
from activity import Activity

def test_itr_1():
    activity = Activity('Brunch')
    
    assert activity.name == 'Brunch'
    assert activity.participants == {}
    
    activity.add_participant('Maria', 20)
    assert activity.participants == {'Maria': 20}
    
    assert activity.total_cost == 20
    
    activity.add_participant('Luther', 40)
    assert activity.participants == {'Maria': 20, 'Luther': 40}
    
    assert activity.total_cost == 60