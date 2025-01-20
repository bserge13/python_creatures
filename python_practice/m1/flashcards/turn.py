class Turn:
    def __init__(self, guess, card):
        self.guess = guess
        self.card = card
    
    def is_correct(self):
        return self.guess == self.card.answer 
    
    def feedback(self):
        if self.is_correct():
            return 'Correct!'
        return 'Incorrect.'