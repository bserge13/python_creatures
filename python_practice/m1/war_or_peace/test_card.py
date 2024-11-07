import pytest 
from card import Card

def test_card_attrs():
    card = Card('heart', 'Jack', 11)

    assert card.suit == 'heart'
    assert card.value == 'Jack'
    assert card.rank == 11