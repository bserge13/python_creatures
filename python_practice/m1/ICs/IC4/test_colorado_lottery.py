import pytest 
from game import Game
from contestant import Contestant

def test_itr_1():
    pick_4 = Game('Pick 4', 2)
    mega = Game('Mega Millions', 5, True)
    
    assert mega.name == 'Mega Millions'
    assert mega.cost == 5
    assert mega.national_drawing == True
    assert pick_4.national_drawing == False
    
    alex = Contestant({'first_name': 'Alexander',
                        'last_name': 'Aigiades',
                        'age': 28,
                        'state_of_residence': 'CO',
                        'spending_money': 10})
    
    assert alex.full_name == 'Alexander Aigiades'
    assert alex.age == 28
    assert alex.state_of_residence == 'CO'
    assert alex.spending_money == 10
    assert alex.is_out_of_state() == False
    assert alex.game_interests == []
    
    alex.add_game_interest('Mega Millions')
    alex.add_game_interest('Pick 4')
    assert alex.game_interests == ['Mega Millions', 'Pick 4']