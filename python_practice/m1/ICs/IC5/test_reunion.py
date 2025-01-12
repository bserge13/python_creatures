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
    assert activity.owed() == {'Maria': 10, 'Luther': -10}
    
    reunion = Reunion('1406 BE')
    
    assert reunion.name == '1406 BE'
    assert reunion.activities == []
    reunion.add_activity(activity)
    assert reunion.activities == [activity]

def test_itr_3():
    reunion = Reunion('2308 BE')
    activity = Activity('Diner and Drinks')
    activity.add_participant('Noelle', 40)
    activity.add_participant('Kam', 20)
    reunion.add_activity(activity)

    assert reunion.event_cost() == 60

    
    # Each Reunion can tell us each participant's name and what they owe for the whole reunion.
    # This should be the combination of what they owe from all activities. Again, a negative value
    # means they are owed money. For example, if "Maria" owes 10 from brunch and is owed 20 from drinks,
    # her final amount owed in the breakout is -10.
    
    # Each Reunion can print a summary of each participant's name and what they owe, separated by a line break.