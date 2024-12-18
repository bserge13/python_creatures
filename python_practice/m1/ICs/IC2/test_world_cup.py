import pytest 
from player import Player
from team import Team

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