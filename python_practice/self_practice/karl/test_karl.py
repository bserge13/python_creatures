import pytest 
from karl import Karl 

def test_attrs():
    karl = Karl()
    
    assert karl.name == 'Karl'
    assert karl.nickname == 'Big Puss'
    assert karl.tired == False
    assert karl.hungry == True
    assert karl.eat_counter == 0 