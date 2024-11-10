class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck

    def has_lost(self):
        return len(self.deck.cards) == 0

    def remove_card(self):
        return self.deck.cards.pop(0)