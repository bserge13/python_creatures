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