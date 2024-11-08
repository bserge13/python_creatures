import pytest
from card import Card
from deck import Deck

card1 = Card('diamond', 'Queen', 12)
card2 = Card('spade', '3', 3)
card3 = Card('heart', 'Ace', 14)
card4 = Card('club', '5', 5)

cards = [card1, card2, card3]
deck = Deck(cards)

def test_deck_cards():
    assert deck.cards == [card1, card2, card3]
    assert deck.cards != [card1, card2, card3, card4]

def test_rank_card_at():
    assert deck.rank_card_at(0) == 12
    assert deck.rank_card_at(2) == 14
    assert deck.rank_card_at(1) == 3

def test_high_ranking_cards():
    assert deck.cards == [card1, card2, card3]
    assert deck.high_ranking_cards() == [card1, card3]
    assert deck.percent_high_ranking() == 66.67

    assert deck.remove_card() == card1
    assert deck.cards == [card2, card3]
    assert deck.percent_high_ranking() == 50.0
    assert deck.high_ranking_cards() == [card3]

    deck.add_card(card4)
    assert deck.cards == [card2, card3, card4]
    assert deck.high_ranking_cards() == [card3]
    assert deck.percent_high_ranking() == 33.33
