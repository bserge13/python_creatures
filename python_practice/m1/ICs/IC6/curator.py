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
    # list of all artists and their photographs (dict)
        ...
    
    def multi_photo_artists(self):
    # list of names of artists who have more than one photograph
        ...
    
    def photos_by_country(self, country):
    # list of Photographs that were taken by a photographer from that country
        ...