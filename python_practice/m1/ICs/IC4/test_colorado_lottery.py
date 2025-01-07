import pytest 
from game import Game
from contestant import Contestant
from colorado_lottery import ColoradoLottery

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

def test_itr_2():
    lottery = ColoradoLottery()
    
    assert lottery.registered_contestants == {}
    assert lottery.winners == []
    assert lottery.current_contestants() == {}
    
    pick_4 = Game('Pick 4', 2)
    mega = Game('Mega Millions', 5, True)
    cash_5 = Game('Cash 5', 1)
    
    alex = Contestant({'first_name': 'Alexander',
                        'last_name': 'Aigiades',
                        'age': 28,
                        'state_of_residence': 'CO',
                        'spending_money': 10})
    sitting_bull = Contestant({'first_name': 'Sitting',
                        'last_name': 'Bull',
                        'age': 17,
                        'state_of_residence': 'PA',
                        'spending_money': 100})
    fred = Contestant({'first_name': 'Frederick',
                        'last_name': 'Douglas',
                        'age': 55,
                        'state_of_residence': 'NY',
                        'spending_money': 20})
    crazy_horse = Contestant({'first_name': 'Crazy',
                        'last_name': 'Horse',
                        'age': 18,
                        'state_of_residence': 'CO',
                        'spending_money': 5})

    alex.add_game_interest('Pick 4')
    alex.add_game_interest('Mega Millions')
    fred.add_game_interest('Mega Millions')
    crazy_horse.add_game_interest('Cash 5')
    crazy_horse.add_game_interest('Mega Millions')
    sitting_bull.add_game_interest('Mega Millions')
    
    assert lottery.interested_and_18(alex, pick_4) == True
    assert lottery.interested_and_18(sitting_bull, mega) == False
    assert lottery.interested_and_18(alex, cash_5) == False
    
    lottery.can_register(alex, pick_4) == True
    lottery.can_register(alex, cash_5) == False
    lottery.can_register(fred, mega) == True
    lottery.can_register(sitting_bull, mega) == False
    lottery.can_register(fred, cash_5) == False

def test_itr_3():
    lottery = ColoradoLottery()
    
    pick_4 = Game('Pick 4', 2)
    mega = Game('Mega Millions', 5, True)
    cash_5 = Game('Cash 5', 1)
    
    red = Contestant({'first_name': 'Red',
                        'last_name': 'Cloud',
                        'age': 28,
                        'state_of_residence': 'CO',
                        'spending_money': 10})
    crazy_horse = Contestant({'first_name': 'Crazy',
                        'last_name': 'Horse',
                        'age': 18,
                        'state_of_residence': 'CO',
                        'spending_money': 2})
    geronimo = Contestant({'first_name': 'Geronimo',
                        'last_name': 'The Great',
                        'age': 55,
                        'state_of_residence': 'NM',
                        'spending_money': 20})
    sitting_bull = Contestant({'first_name': 'Sitting',
                        'last_name': 'Bull',
                        'age': 17,
                        'state_of_residence': 'ND',
                        'spending_money': 15})
    
    red.add_game_interest('Pick 4')
    crazy_horse.add_game_interest('Pick 4')
    geronimo.add_game_interest('Pick 4')
    sitting_bull.add_game_interest('Pick 4')

    red.add_game_interest('Cash 5')
    crazy_horse.add_game_interest('Cash 5')
    geronimo.add_game_interest('Cash 5')
    sitting_bull.add_game_interest('Cash 5')

    red.add_game_interest('Mega Millions')
    crazy_horse.add_game_interest('Mega Millions')
    geronimo.add_game_interest('Mega Millions')
    sitting_bull.add_game_interest('Mega Millions')

    lottery.register_contestant(red, mega)
    lottery.register_contestant(red, pick_4)
    assert lottery.registered_contestants == {red: [mega, pick_4]}
    assert lottery.current_contestants() == {pick_4: [red.full_name], mega: [red.full_name]}
    assert lottery.eligible_contestants() == [red]
    
    lottery.register_contestant(crazy_horse, pick_4)
    lottery.register_contestant(crazy_horse, cash_5)
    assert lottery.registered_contestants == {red: [mega, pick_4], crazy_horse: [pick_4, cash_5]}
    assert lottery.current_contestants() == {pick_4: [red.full_name, crazy_horse.full_name], mega: [red.full_name], cash_5: [crazy_horse.full_name]}
    assert lottery.eligible_contestants() == [crazy_horse, red]

    lottery.register_contestant(geronimo, pick_4)
    lottery.register_contestant(geronimo, mega)
    lottery.register_contestant(geronimo, cash_5)
    assert lottery.registered_contestants == {red: [mega, pick_4], crazy_horse: [pick_4, cash_5], geronimo: [mega]}
    assert lottery.current_contestants() == {pick_4: [red.full_name, crazy_horse.full_name], mega: [red.full_name, geronimo.full_name], cash_5: [crazy_horse.full_name]}
    assert lottery.eligible_contestants() == [crazy_horse, geronimo, red]
    
    lottery.register_contestant(sitting_bull, pick_4)
    lottery.register_contestant(sitting_bull, mega)
    lottery.register_contestant(sitting_bull, cash_5)
    assert lottery.registered_contestants == {red: [mega, pick_4], crazy_horse: [pick_4, cash_5], geronimo: [mega]}
    assert lottery.current_contestants() == {pick_4: [red.full_name, crazy_horse.full_name], mega: [red.full_name, geronimo.full_name], cash_5: [crazy_horse.full_name]}
    assert lottery.eligible_contestants() == [crazy_horse, geronimo, red]


def test_itr_4():
    ...