import pytest 
from loki import Loki

def test_attrs():
    loki = Loki()
    
    assert loki.name == 'Loki'
    assert loki.breed == 'Couch Hippo'
    assert loki.nickname == 'Little Puss'
    assert loki.hungry == True