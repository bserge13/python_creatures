class Curator:
    def __init__(self):
        self.artists = []
        self.photographs = []
    
    def add_artist(self, artist):
        self.artists.append(artist)
    
    def add_photograph(self, photo):
        self.photographs.append(photo)
    
    def find_artist_by_id(self, id):
        for artist in self.artists:
            if artist.id == id:
                return artist
        return None
    
    def library(self):
    # list of all artists and their photographs (dict)
        library = {}
        for artis in self.artists:
            ...
    
    def multi_photo_artists(self):
    # list of names of artists who have more than one photograph
        ...
    
    def photos_by_country(self, country):
    # list of Photographs that were taken by a photographer from that country
        ...