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
        return 'basic'

    def winner(self):
        if self.type() == 'basic':
            return max(self.player1, self.player2, key=lambda player: player.deck.rank_card_at(0))
        elif self.type() == 'war':
            return max(self.player1, self.player2, key=lambda player: player.deck.rank_card_at(2))
        return 'No Winner'

    def pile_cards(self):
        self.spoils_of_war.extend([self.player1.remove_card(), self.player2.remove_card()])

    def award_spoils(self, winner):
        for card in self.spoils_of_war:
            winner.deck.add_card(card)
