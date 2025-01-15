class Artist:
    def __init__(self, attrs):
        self.id = attrs['id']
        self.name = attrs['name']
        self.born = attrs['born']
        self.died = attrs['died']
        self.country = attrs['country']
    
    def age_at_death(self):
        return int(self.died) - int(self.born)