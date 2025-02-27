import pytest 
from loki import Loki

loki = Loki()

def test_attrs():    
    assert loki.name == 'Loki'
    assert loki.breed == 'Couch Hippo'
    assert loki.nickname == 'Little Puss'
    assert loki.hungry == True