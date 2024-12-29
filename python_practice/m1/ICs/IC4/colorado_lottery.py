class ColoradoLottery:
    def __init__(self):
        self.registered_contestants = {}
        self.winners = []
        self.current_contestants = {}
    
    def interested_and_18(self, contestant, game):
        return contestant.age >= 18 and game.name in contestant.game_interests
    
    def can_register(self, contestant, game):
        if self.interested_and_18(contestant, game):
            if not contestant.is_out_of_state() or game.national_drawing == True:
                return True
    
    def register_contestant(self, contestant, game):
        if self.can_register(contestant, game):
            self.registered_contestants[contestant] = game
    
    def eligible_contestants(self):
        ...