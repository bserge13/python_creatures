import pytest 
from activity import Activity
from reunion import Reunion

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

def test_itr_2():
    activity = Activity('Brunch')
    activity.add_participant('Maria', 20)
    activity.add_participant('Luther', 40)

    assert activity.total_cost == 60
    assert activity.split() == 30
    # assert activity.owed() == {'Maria': 10, 'Luther': -10}
    
    reunion = Reunion('1406 BE')
    
    assert reunion.name == '1406 BE'
    assert reunion.activities == []
    reunion.add_activity(activity)
    assert reunion.activities == [activity]
