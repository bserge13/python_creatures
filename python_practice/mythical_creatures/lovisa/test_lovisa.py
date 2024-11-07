import pytest
from lovisa import Lovisa

def test_has_title():
    lovisa = Lovisa('Lovisa the Swedish Goddess')
    assert lovisa.title == 'Lovisa the Swedish Goddess'

def test_default_brilliant():
    lovisa = Lovisa('Lovisa the Swedish Goddess')

    assert lovisa.characteristics == ['brilliant']
    assert lovisa.is_brilliant() == True

def test_more_characteristics():
    lovisa = Lovisa('Lovisa the friend', ['brilliant', 'kind'])

    assert lovisa.characteristics == ['brilliant', 'kind']
    assert lovisa.is_brilliant() == True
    assert lovisa.is_kind() == True

def test_says_sparkly_things():
    lovisa = Lovisa('Lovisa the Loved')

    assert lovisa.say('Wonderful!') == '**;* Wonderful! **;*'
    assert lovisa.say('You are doing great!') == '**;* You are doing great! **;*'
