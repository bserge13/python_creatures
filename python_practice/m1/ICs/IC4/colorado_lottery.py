class ColoradoLottery:
    def __init__(self):
        self.registered_contestants = {}
        self.winners = []
        self.current_contestants = {}
    
    def interested_and_18(self, contestant, game):
        if contestant.age >= 18:
            if game.name in contestant.game_interests:
                if not contestant.is_out_of_state() or game.national_drawing == True:
                    return True
        return False
    
    def can_register(self, contestant, game):
        ...