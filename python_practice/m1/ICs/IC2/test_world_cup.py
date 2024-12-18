import pytest 
from player import Player

def test_itr1():
    player = Player({'name': 'Luka Modric', 'position': 'midfielder'})
    
    assert player.name == 'Luka Modric'
    assert player.position == 'midfielder'