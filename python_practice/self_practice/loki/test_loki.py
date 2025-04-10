import pytest 
from loki import Loki
from friend import Friend


def test_attrs():    
    loki = Loki()
    assert loki.name == 'Loki'
    assert loki.breed == 'Couch Hippo'
    assert loki.nickname == 'Little Puss'
    assert loki.hungry == True
    assert loki.eat_counter == 0

def test_functions():
    loki = Loki()

    loki.eat()
    loki.eat()
    assert loki.eat_counter == 2

def test_friends():
    loki = Loki()

    assert loki.has_friends() == False
    assert loki.friends == []

    karl = Friend('Karl')

    loki.add_friend(karl)
    assert loki.has_friends() == True
    assert loki.friends == [karl]
    assert loki.friends[0].name == 'Karl'

def test_friend_attrs():
    loki = Loki()
    karl = Friend('Karl')

    assert karl.tired == False
    assert karl.play_count == 0 
    assert karl.demenior() == 'Playful'
    assert karl.age == 1

    loki.add_friend(karl)
    karl.play_with(loki)
    assert karl.play_count == 1
    assert karl.demenior() == 'Playful'

    karl.play_with(loki)
    karl.play_with(loki)
    assert karl.play_count == 3
    assert karl.demenior() == 'Tired'

def test_loki_friend_attrs():
    loki = Loki()
    karl = Friend('Karl')

    loki.add_friend(karl)
    assert karl.play_count == 0
    karl.play_with(loki)
    assert karl.play_count == 1

    loki.play_with(karl)
    assert karl.play_count == 2
    assert karl.demenior() == 'Playful'

    karl.play_with(loki)
    loki.play_with(karl)
    assert karl.demenior() == 'Tired'

def test_play_with():
    loki = Loki()
    karl = Friend('Karl')

    assert loki.friends == []
    loki.play_with(karl)
    assert loki.friends == [karl]

    cowboy = Friend('Cowboy')
    assert cowboy.play_count == 0
    assert cowboy.play_with(loki) == "We're not friends"

    assert cowboy.demenior() == 'Playful'
    assert cowboy.tired == False

    loki.play_with(cowboy)
    cowboy.play_with(loki)
    assert cowboy.age == 1
    cowboy.play_with(loki)

    assert cowboy.demenior() == 'Tired'
    assert cowboy.tired == True
    assert cowboy.age == 2
    assert loki.friends == [karl, cowboy]

def test_loki_speak():
    loki = Loki()
    karl = Friend('Karl')
    cowboy = Friend('Cowboy')

    assert loki.friends == []
    assert loki.speak() == 'I have no friends (womp womp)'

    loki.add_friend(karl)
    loki.add_friend(cowboy)
    assert loki.friends == [karl, cowboy]

    assert loki.speak() == f"Hi, {karl.name}! Hi, {cowboy.name}!"

def test_karl_speak():
    loki = Loki()
    karl = Friend('Karl')

    assert karl.speak(loki) == 'Go away, dumb dumb'
    loki.add_friend(karl)
    assert karl.speak(loki) == f"I tolerate you, {loki.nickname}"