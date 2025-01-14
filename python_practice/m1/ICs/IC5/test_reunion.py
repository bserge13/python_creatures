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

    activity_1.add_participant('Noelle', 15)
    activity_1.add_participant('Kam', 10)

    activity_2.add_participant('Noelle', 30)
    activity_2.add_participant('Tommy', 20)
    activity_2.add_participant('Kam', 15)
    
    reunion.add_activity(activity_1)
    reunion.add_activity(activity_2)

    assert reunion.event_cost() == 90
    
    assert activity_1.owed() == {'Kam': 2.5, 'Noelle': -2.5}
    assert activity_2.owed() == {'Noelle': -8.33, 'Tommy': 1.67, 'Kam': 6.67}
    assert reunion.split_bill() == {'Noelle': -10.83, 'Kam': 9.17, 'Tommy': 1.67}
    
    assert reunion.print_bill() == 'Noelle owes $-10.83\nKam owes $9.17\nTommy owes $1.67'
    # Each Reunion can print a summary of each participant's name and what they owe, separated by a line break.