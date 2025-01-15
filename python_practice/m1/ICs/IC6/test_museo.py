import pytest
from artist import Artist
from photograph import Photograph
from curator import Curator

def test_itr_1():
    photo_attrs = {
        'id': '1',
        'name': 'Rue Mouffetard, Paris (Boy with Bottles)',
        'artist_id': '4',
        'year': '1954'
    }
    photograph = Photograph(photo_attrs)
    
    assert photograph.id == '1'
    assert photograph.name == 'Rue Mouffetard, Paris (Boy with Bottles)'
    assert photograph.artist_id == '4'
    assert photograph.year == '1954'
    
    artist_attrs = {
            'id': '2',
            'name': 'Ansel Adams',
            'born': '1902',
            'died': '1984',
            'country': 'United States'
        }
    artist = Artist(artist_attrs)
    
    assert artist.id == '2'
    assert artist.name == 'Ansel Adams'
    assert artist.born == '1902'
    assert artist.died == '1984'
    assert artist.country == 'United States'
    assert artist.age_at_death() == 82

def test_itr_2():
    curator = Curator()
    
    assert curator.photographs == []