import pytest 
from loki import Loki
from friend import Friend

loki = Loki()

def test_attrs():    
    assert loki.name == 'Loki'
    assert loki.breed == 'Couch Hippo'
    assert loki.nickname == 'Little Puss'
    assert loki.hungry == True
    assert loki.eat_counter == 0

def test_functions():
    loki.eat()
    loki.eat()
    assert loki.eat_counter == 2

def test_friends():
    assert loki.has_friends() == False
    assert loki.friends == []

    karl = Friend('Karl')
    
    loki.add_friend(karl)
    assert loki.has_friends() == True
    assert loki.friends == [karl]
    assert loki.friends[0].name == 'Karl'

def test_friend_attrs():
    karl = Friend('Karl')

    assert karl.tired == False
    assert karl.play_count == 0 
    assert karl.demenior == 'Playful'
    assert karl.age == 1


    karl.play_with(loki)
    assert karl.play_count == 1
    assert karl.demenior == 'Playful'

    karl.play_with(loki)
    karl.play_with(loki)
    assert karl.play_count == 3
    # assert karl.demenior == 'Tired'