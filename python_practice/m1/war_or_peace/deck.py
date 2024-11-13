class Deck:
    def __init__(self, cards):
        self.cards = cards

    def rank_card_at(self, pos):
        return self.cards[pos].rank

    def high_ranking_cards(self):
    # list comprehension refactor
        return [card for card in self.cards if card.rank >= 11]
        # cards = []
        # for card in self.cards:
        #     if card.rank >= 11:
        #         cards.append(card)
        # return cards

    def percent_high_ranking(self):
        return round(float(len(self.high_ranking_cards()) * 100) / float(len(self.cards)), 2)

    def remove_card(self):
        return self.cards.pop(0)

    def add_card(self, card):
        self.cards.append(card)
