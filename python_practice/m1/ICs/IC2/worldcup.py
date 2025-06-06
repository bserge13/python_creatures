class WorldCup:
    def __init__(self, year, teams):
        self.year = year
        self.teams = teams
    
    def active_players_by_position(self, position):
        # players = []
        # for team in self.teams:
        #     if not team.is_eliminated():
        #         for player in team.players:
        #             if player.position == position:
        #                 players.append(player)
        # return players
        return [
            player
            for team in self.teams if not team.is_eliminated()
            for player in team.players if player.position == position
        ]
    
    def all_players_by_position(self):
        lineup = {
            'forward': [],
            'midfieldr': [],
            'defender': []
        }
        for team in self.teams:
            for player in team.players:
                if player.position in lineup:
                    lineup[player.position] = player
        return lineup