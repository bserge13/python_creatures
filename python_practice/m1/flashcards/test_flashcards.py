import pytest 
from card import Card
from turn import Turn

def test_itr_1():
    card = Card('What is the capital of Alaska?', 'Juneau', 'Geography')
    
    assert card.question == 'What is the capital of Alaska?'
    assert card.answer == 'Juneau'
    assert card.category == 'Geography'
    
    turn = Turn('Juneau', card)
    
    assert turn.card == card
    assert turn.guess == 'Juneau'
    assert turn.is_correct() == True
    assert turn.feedback() == 'Correct!'

def test_itr_2():
    ...