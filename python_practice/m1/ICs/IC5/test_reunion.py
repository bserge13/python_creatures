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
    activity_1 = Activity('Diner and Comedy Show')
    activity_2 = Activity('Drinks and Games')

    activity_1.add_participant('Noelle', 10)
    activity_1.add_participant('Kam', 10)

    activity_2.add_participant('Noelle', 30)
    activity_2.add_participant('Tommy', 20)
    activity_2.add_participant('Kam', 15)
    
    reunion.add_activity(activity_1)
    reunion.add_activity(activity_2)

    assert reunion.event_cost() == 85
    
    # assert activity_1.owed() == {'Kam': 0, 'Noelle': 0} PASSING
    # assert activity_2.owed() == {'Noelle': -8.33, 'Tommy': 1.67, 'Kam': 6.67} PASSING
    # assert reunion.split_bill() == {}
    
    # Each Reunion can tell us each participant's name and what they owe for the whole reunion.
    # This should be the combination of what they owe from all activities. Again, a negative value
    # means they are owed money. For example, if "Maria" owes 10 from brunch and is owed 20 from drinks,
    # her final amount owed in the breakout is -10.
    
    # Each Reunion can print a summary of each participant's name and what they owe, separated by a line break.