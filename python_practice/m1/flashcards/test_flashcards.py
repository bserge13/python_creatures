import pytest 
from card import Card
from turn import Turn

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
    ...