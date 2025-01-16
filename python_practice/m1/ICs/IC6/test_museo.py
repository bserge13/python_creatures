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
    artist_1 = Artist({
        'id': '1',
        'name': 'Henri Cartier-Bresson',
        'born': '1908',
        'died': '2004',
        'country': 'France'
    })
    artist_2 = Artist({
        'id': '2',
        'name': 'Ansel Adams',
        'born': '1902',
        'died': '1984',
        'country': 'United States'
    })
    
    assert curator.artists == []
    
    curator.add_artist(artist_1)
    curator.add_artist(artist_2)
    
    assert curator.artists == [artist_1, artist_2]
    assert curator.find_artist_by_id('1')

def test_itr_3():
    curator = Curator()
    artist_1 = Artist({
        'id': '1',
        'name': 'Henri Cartier-Bresson',
        'born': '1908',
        'died': '2004',
        'country': 'France'
    })
    artist_2 = Artist({
        'id': '2',
        'name': 'Ansel Adams',
        'born': '1902',
        'died': '1984',
        'country': 'United States'
    })
    photo_1 = Photograph({
        'id': '1',
        'name': 'Rue Mouffetard, Paris (Boy with Bottles)',
        'artist_id': '1',
        'year': '1954'
    })
    photo_2 = Photograph({
        'id': '2',
        'name': 'The Great Wave of Loki',
        'artist_id': '2',
        'year': '1970'
    })
    photo_3 = Photograph({
        'id': '3',
        'name': 'Hold Them Accountable (Karl wanting for Snacks)',
        'artist_id': '2',
        'year': '1969'
    })

# A Curator can return a list of all artists and their photographs
    assert curator.library() == [{artist_1: [photo_1], artist_2: [photo_2, photo_3]}]
# A Curator can return a list of names of artists who have more than one photograph
    assert curator.multi_photo_artists() == [artist_2]
# A Curator can return a list of Photographs that were taken by a photographer from that country
    assert curator.photos_by_country('France') == [photo_1]
    assert curator.photos_by_country('united states') == [photo_2, photo_3]
