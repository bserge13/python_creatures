class Team:
    def __init__(self, country):
        self.country = country
        self.eliminated = False
        self.players = []
    
    def is_eliminated(self):
        return self.eliminated

    def add_player(self, player):
        self.players.append(player)
    
    def players_by_position(self, position):
        return [player for player in self.players if player.position == position]