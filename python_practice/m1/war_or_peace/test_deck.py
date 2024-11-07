import pytest
from card import Card
from deck import Deck

def test_deck_attrs():
    card1 = Card('diamond', 'Queen', 12)
    card2 = Card('spade', '3', 3)
    card3 = Card('heart', 'Ace', 14)
    cards = [card1, card2, card3]
    deck = Deck(cards)

    assert deck.cards == [card1, card2, card3]
    assert deck.rank_card_at(0) == 12
    assert deck.rank_card_at(2) == 14
    assert deck.high_ranking_cards() == [card1, card3]
    assert deck.percent_high_ranking() == 66.67
    assert deck.remove_card() == card1
    assert deck.cards == [card2, card3]
    assert deck.high_ranking_cards() == [card3]
    assert deck.percent_high_ranking() == 50.0

    card4 = Card('club', '5', 5)
    deck.add_card(card4)
    assert deck.cards == [card2, card3, card4]
    assert deck.high_ranking_cards() == [card3]
    assert deck.percent_high_ranking() == 33.33