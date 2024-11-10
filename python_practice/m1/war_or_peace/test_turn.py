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

deck1 = Deck([card1, card2, card5, card8])
deck2 = Deck([card3, card4, card6, card7])

player1 = Player('Loki', deck1)
player2 = Player('Karl', deck2)

turn = Turn(player1, player2)

def test_turn_attrs():
    assert turn.player1 == player1
    assert turn.player1.name == 'Loki'

    assert turn.player2 == player2
    assert turn.player2.name == 'Karl'

def test_turn_class_functions():
    assert turn.type() == 'basic'

    winner = turn.winner()
    assert winner.name == 'Loki'

    turn.pile_cards()
    assert turn.spoils_of_war == [card1, card3]
    turn.award_spoils(winner)

    assert player1.deck == [card2, card5, card8, card1, card3]
    assert player2.deck == [card4, card6, card7]