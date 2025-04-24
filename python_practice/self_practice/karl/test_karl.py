import pytest 
from karl import Karl 

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