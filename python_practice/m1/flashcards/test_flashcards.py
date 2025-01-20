import pytest 
from card import Card
from turn import Turn
from deck import Deck

def test_itr_1():
    card = Card('What is the capital of Alaska?', 'Juneau', 'Geography')
    
    assert card.question == 'What is the capital of Alaska?'
    assert card.answer == 'Juneau'
    assert card.category == 'Geography'
    
    turn_1 = Turn('Juneau', card)
    turn_2 = Turn('Juniper', card)
    
    assert turn_1.card == card
    assert turn_1.guess == 'Juneau'
    assert turn_1.is_correct() == True
    assert turn_1.feedback() == 'Correct!'
    
    assert turn_2.is_correct() == False
    assert turn_2.feedback() == 'Incorrect.'

def test_itr_2():
    card_1 = Card('What is the capital of Alaska?', 'Juneau', 'Geography')
    card_2 = Card('The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?', 'Mars', 'STEM')
    card_3 = Card('Describe in words the exact direction that is 697.5° clockwise from due north?', 'North north west', 'STEM')
    
    cards = [card_1, card_2, card_3]
    deck = Deck(cards)
    
    assert deck.cards == [card_1, card_2, card_3]
    assert deck.count() == 3
    # assert deck.cards_in_category('STEM') == [card_2, card_3]
    # assert deck.cards_in_category('Geography') == [card_1]
    # assert deck.cards_in_category('Pop Culture') == []
    