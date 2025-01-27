class Round:
    def __init__(self, deck):
        self.deck = deck
        self.turns = []
    
    def current_card(self):
        return self.deck.cards[0]