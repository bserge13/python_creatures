class Photograph:
    def __init__(self, attrs):
        self.id = attrs['id']
        self.name = attrs['name']
        self.artist_id = attrs['artist_id']
        self.year = attrs['year']