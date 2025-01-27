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
    
    def number_correct_by_category(self, category):
        category_cards = []
        for turn in self.turns:
            if turn.card.category == category and turn.is_correct():
                category_cards.append(turn)
        return len(category_cards)
    
    def percent_correct(self):
        if len(self.turns) == 0:
            return 0
        return (self.number_correct() / len(self.turns)) * 100