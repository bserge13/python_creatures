import pytest 
from player import Player
from team import Team
from worldcup import WorldCup

def test_itr_1():
    player = Player({'name': 'Luka Modric', 'position': 'midfielder'})
    
    assert player.name == 'Luka Modric'
    assert player.position == 'midfielder'

def test_itr_2():
    team = Team('France')
    
    assert team.country == 'France'
    assert team.is_eliminated() == False
    
    team.eliminated = True
    assert team.is_eliminated() == True
    assert team.players == []
    
    mbappe = Player({'name': 'Kylian Mbappe', 'position': 'forward'})
    pogba = Player({'name': 'Paul Pogba', 'position': 'midfielder'})
    
    team.add_player(mbappe)
    team.add_player(pogba)
    
    assert team.players == [mbappe, pogba]
    assert team.players_by_position('midfielder') == [pogba]
    assert team.players_by_position('defender') == []

def test_itr_3():
    france = Team('France')
    croatia = Team('Croatia')

    mbappe = Player({'name': 'Kylian Mbappe', 'position': 'forward'})
    pogba = Player({'name': 'Paul Pogba', 'position': 'midfielder'})
    modric = Player({'name': 'Luka Modric', 'position': 'midfielder'})
    vida = Player({'name': 'Domagoj Vida', 'position': 'defender'})

    world_cup = WorldCup(2018, [france, croatia])

    france.add_player(mbappe)
    france.add_player(pogba)
    croatia.add_player(modric)
    croatia.add_player(vida)
    
    assert world_cup.year == 2018
    assert world_cup.teams == [france, croatia]
    assert world_cup.active_players_by_position('midfielder') == [pogba, modric]
    
    croatia.eliminated = True
    assert world_cup.active_players_by_position('midfielder') == [pogba]

def test_itr_4():
    france = Team('France')
    croatia = Team('Croatia')

    mbappe = Player({'name': 'Kylian Mbappe', 'position': 'forward'})
    pogba = Player({'name': 'Paul Pogba', 'position': 'midfielder'})
    modric = Player({'name': 'Luka Modric', 'position': 'midfielder'})
    vida = Player({'name': 'Domagoj Vida', 'position': 'defender'})

    world_cup = WorldCup(2018, [france, croatia])

    france.add_player(mbappe)
    france.add_player(pogba)
    croatia.add_player(modric)
    croatia.add_player(vida)

    world_cup.all_players_by_position() == {
        'forward': [mbappe],
        'midfielder': [pogba, modric],
        'defender': [vida]
    }