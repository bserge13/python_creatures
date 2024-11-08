import pytest 
from card import Card
from deck import Deck
from player import Player

card1 = Card('diamond', 'Queen', 12)
card2 = Card('spade', '3', 3)
card3 = Card('heart', 'Ace', 14)

deck = Deck([card1, card2, card3])
player = Player('Clarisa', deck)

def test_player_attrs():
    assert player.name == 'Clarisa'
    assert player.deck == [card1, card2, card3]

def test_has_lost():
    assert player.deck == [card1, card2, card3]
    assert player.has_lost() == False
    assert player.remove_card() == card1

    assert player.deck == [card2, card3]
    assert player.has_lost() == False
    assert player.remove_card() == card2
    
    assert player.deck == [card3]
    assert player.has_lost() == False
    assert player.remove_card() == card3

    assert player.deck == []
    assert player.has_lost() == False
