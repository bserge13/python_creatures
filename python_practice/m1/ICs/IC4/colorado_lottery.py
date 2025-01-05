class ColoradoLottery:
    def __init__(self):
        self.registered_contestants = {}
        self.winners = []
    
    def interested_and_18(self, contestant, game):
        return contestant.age >= 18 and game.name in contestant.game_interests
    
    def can_register(self, contestant, game):
        if self.interested_and_18(contestant, game):
            if not contestant.is_out_of_state() or game.national_drawing == True:
                return True
    
    def register_contestant(self, contestant, game):
        if self.can_register(contestant, game):
            if contestant not in self.registered_contestants:
                self.registered_contestants[contestant] = []
            self.registered_contestants[contestant].append(game)
    
    def current_contestants(self):
        current_players = {}
        for contestant,games in self.registered_contestants.items():
            for game in games:
                if game not in current_players:
                    current_players[game] = []
                current_players[game].append(contestant)
        return current_players
        # Dict where key is a Game object and the values is a list of contestant names
    
    def eligible_contestants(self):
        # return [contestant for contestant,game in self.registered_contestants.items() if contestant.spending_money > game.cost]
        elg_contestant = []
        for contestant,games in self.registered_contestants.items():
            for game in games:
                if contestant.spending_money > game.cost:
                    elg_contestant.append(contestant)
        return sorted(list(set(elg_contestant)), key=lambda x: x.full_name)
        # List of Contestants who've been registered to play a given game and that have more spending_money than cost