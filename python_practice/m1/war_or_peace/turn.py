class Turn:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.spoils_of_war = []

    def type(self):
        if self.player1.deck.rank_card_at(0) == self.player2.deck.rank_card_at(0):
            if self.player1.deck.rank_of_card_at(2) == self.player2.deck.rank_of_card_at(2):
                return 'mutually_assured_destruction'
            return 'war'
        else:
            return 'basic'

    def winner(self):
        players = [self.player1, self.player2]
        if self.type() == 'basic':
            # return the player whose card is higher than their opponents'
            winner = sorted(players, key=lambda player: player.deck.rank_card_at(0), reverse=True)
            return winner[0]
        elif self.type() == 'war':
            ...
            # return the player whose .deck.rank_of_card(2) is higher than their opponents'
        else:
            return 'No Winner'
