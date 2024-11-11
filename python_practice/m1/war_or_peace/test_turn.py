import pytest 
from card import Card
from deck import Deck
from player import Player
from turn import Turn

card1 = Card('heart', 'Jack', 11)
card2 = Card('heart', '10', 10)
card3 = Card('heart', '9', 9)
card4 = Card('diamond', 'Jack', 11)
card5 = Card('heart', '8', 8)
card6 = Card('diamond', 'Queen', 12)
card7 = Card('heart', '3', 3)
card8 = Card('diamond', '2', 2)
card9 = Card('diamond', '8', 8)

def test_turn_type_basic():
    deck1 = Deck([card1, card2, card5, card8])
    deck2 = Deck([card3, card4, card6, card7])

    player1 = Player('Loki', deck1)
    player2 = Player('Karl', deck2)

    turn = Turn(player1, player2)

    assert turn.type() == 'basic'

    winner = turn.winner()
    assert winner.name == 'Loki'

    turn.pile_cards()
    assert turn.spoils_of_war == [card1, card3]
    turn.award_spoils(winner)

    assert player1.deck.cards == [card2, card5, card8, card1, card3]
    assert player2.deck.cards == [card4, card6, card7]

def test_turn_type_war():
    deck1 = Deck([card1, card2, card5, card8])
    deck2 = Deck([card4, card3, card6, card7])

    player1 = Player('Loki', deck1)
    player2 = Player('Karl', deck2)

    turn = Turn(player1, player2)

    assert turn.type() == 'war'

    winner = turn.winner()
    assert winner.name == 'Karl'

    turn.pile_cards()
    assert turn.spoils_of_war == [card1, card2, card5, card4, card3, card6]
    turn.award_spoils(winner)

    assert player1.deck.cards == [card8]
    assert player2.deck.cards == [card7, card1, card2, card5, card4, card3, card6]

def test_turn_type_war():
    deck1 = Deck([card1, card2, card5, card8])
    deck2 = Deck([card4, card3, card9, card7])

    player1 = Player('Loki', deck1)
    player2 = Player('Karl', deck2)

    turn = Turn(player1, player2)

    assert turn.type() == 'mutually_assured_destruction'

    winner = turn.winner()
    assert winner == 'No Winner'

    turn.pile_cards()
    assert turn.spoils_of_war == []

    assert player1.deck.cards == [card8]
    assert player2.deck.cards == [card7]
