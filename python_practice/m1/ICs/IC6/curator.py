class Curator:
    def __init__(self):
        self.artists = []
    
    def add_artist(self, photo):
        self.artists.append(photo)
    
    def find_artist_by_id(self, id):
        for artist in self.artists:
            if artist.id == id:
                return artist
        return None
    
    def library(self):
        ...
    
    def multi_photo_artists(self):
        ...
    
    def photos_by_country(self, country):
        ...