from turn import Turn 

class Round:
    def __init__(self, deck):
        self.deck = deck
        self.turns = []
    
    def current_card(self):
        return self.deck.cards[0]
    
    def take_turn(self, guess):
        attempt = Turn(guess, self.current_card())
        self.turns.append(attempt)
        # self.deck.cards.pop()
        return attempt
    
    def number_correct(self):
        return len(self.turns)