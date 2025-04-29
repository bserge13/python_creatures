import pytest 
from karl import Karl
from friend import Friend

def test_attrs():
    karl = Karl()
    
    assert karl.name == 'Karl'
    assert karl.nickname == 'Big Puss'
    assert karl.tired == False
    assert karl.hungry == True
    assert karl.treat_counter == 0 

def test_meow():
    karl = Karl()
    
    karl.meow()
    assert karl.treat_counter == 1
    assert karl.hungry == True
    assert karl.tired == False
    
    karl.meow()
    assert karl.treat_counter == 2
    assert karl.hungry == True
    assert karl.tired == False

    karl.meow()
    assert karl.treat_counter == 3
    assert karl.hungry == False
    assert karl.tired == True

def test_speak():
    karl = Karl()

    assert karl.speak() == 'I am Karl, hear me ROAR!'
    assert karl.speak('Loki') == 'I am Karl, hear me ROAR, Loki!'

def test_friend_play():
    karl = Karl()
    loki = Friend()

    