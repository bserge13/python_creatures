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
        portfolio = {artist.id: [] for artist in self.artists}
        
        for photo in self.photographs:
            if photo.artist_id in portfolio:
                portfolio[photo.artist_id].append(photo)
        
        library = []
        for artist in self.artists:
            library.append({artist: portfolio[artist.id]})
        
        return library
    
    def multi_photo_artists(self):
    # list of names of artists who have more than one photograph
        ...
    
    def photos_by_country(self, country):
    # list of Photographs that were taken by a photographer from that country
        ...