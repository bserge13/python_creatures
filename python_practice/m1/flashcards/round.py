from turn import Turn 

class Round:
    def __init__(self, deck):
        self.deck = deck
        self.turns = []
        self.current_card_index = 0
    
    def current_card(self):
        return self.deck.cards[self.current_card_index]
    
    def take_turn(self, guess):
        attempt = Turn(guess, self.current_card())
        self.turns.append(attempt)
        
        self.current_card_index += 1
        
        return attempt
    
    def number_correct(self):
        return len([turn for turn in self.turns if turn.is_correct()])