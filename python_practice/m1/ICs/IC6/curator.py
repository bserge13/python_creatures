class Curator:
    def __init__(self):
        self.photographs = []
    
    def add_artist(self, photo):
        self.photographs.append(photo)
    
    def find_artist_by_id(self, id):
        for photo in self.photographs:
            ...