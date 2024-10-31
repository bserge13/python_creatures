import pytest
from unicorn import Unicorn

def test_has_name():
    unicorn1 = Unicorn('Robert')
    unicorn2 = Unicorn('Benny')

    assert isinstance(unicorn1, Unicorn)
    assert isinstance(unicorn2, Unicorn)
    assert unicorn1.name == 'Robert'
    assert unicorn2.name == 'Benny'

def test_default_silver():
    unicorn = Unicorn('Loki')

    assert unicorn.color == 'silver'
    assert unicorn.is_silver() == True

def test_not_always_silver():
    unicorn1 = Unicorn('Loki')
    unicorn2 = Unicorn('Karl', 'purple')

    assert unicorn1.color == 'silver'
    assert unicorn1.is_silver() == True

    assert unicorn2.color == 'purple'
    assert unicorn2.is_silver() == False

def test_says_sparkly_stuff():
    unicorn = Unicorn('Nova')

    assert unicorn.say('Wonderful') == '**;* Wonderful! **;*'
    assert unicorn.say('Bye, Felicia') == '**;* Bye, Felicia! **;*'
