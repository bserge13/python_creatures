import random
import turn, player, deck, card

all_cards = [
    card.Card('diamond', '1', 1), card.Card('diamond', '2', 2), card.Card('diamond', '3', 3),
    card.Card('diamond', '4', 4), card.Card('diamond', '5', 5), card.Card('diamond', '6', 6),
    card.Card('diamond', '7', 7), card.Card('diamond', '8', 8), card.Card('diamond', '9', 9),
    card.Card('diamond', '10', 10), card.Card('diamond', 'Jack', 11), card.Card('diamond', 'Queen', 12),
    card.Card('diamond', 'King', 13), card.Card('diamond', 'Ace', 14), card.Card('heart', '1', 1),
    card.Card('heart', '2', 2), card.Card('heart', '3', 3), card.Card('heart', '4', 4),
    card.Card('heart', '5', 5), card.Card('heart', '6', 6), card.Card('heart', '7', 7),
    card.Card('heart', '8', 8), card.Card('heart', '9', 9), card.Card('heart', '10', 10),
    card.Card('heart', 'Jack', 11), card.Card('heart', 'Queen', 12), card.Card('heart', 'King', 13),
    card.Card('heart', 'Ace', 14), card.Card('spade', '1', 1), card.Card('spade', '2', 2),
    card.Card('spade', '3', 3), card.Card('spade', '4', 4), card.Card('spade', '5', 5),
    card.Card('spade', '6', 6), card.Card('spade', '7', 7), card.Card('spade', '8', 8),
    card.Card('spade', '9', 9), card.Card('spade', '10', 10), card.Card('spade', 'Jack', 11),
    card.Card('spade', 'Queen', 12), card.Card('spade', 'King', 13), card.Card('spade', 'Ace', 14),
    card.Card('club', '1', 1), card.Card('club', '2', 2), card.Card('club', '3', 3),
    card.Card('club', '4', 4), card.Card('club', '5', 5), card.Card('club', '6', 6),
    card.Card('club', '7', 7), card.Card('club', '8', 8), card.Card('club', '9', 9),
    card.Card('club', '10', 10), card.Card('club', 'Jack', 11), card.Card('club', 'Queen', 12),
    card.Card('club', 'King', 13), card.Card('club', 'Ace', 14),
]

def main():
    start = input(
        "Welcome to War! (or Peace) This game will be played with 52 cards.\nThe players today are Loki and Karl.\nType 'GO' to start the game! ").upper()
    if start == 'GO':
        print(new_game())

def new_game():
    full_deck = random.shuffle(all_cards)
    half = len(full_deck) // 2
    player1 = player.Player('Loki', full_deck[:half])
    player2 = player.Player('Karl', full_deck[half:])
    games = turn.Turn(player1, player2)

    for match in games:
        print(f"Turn 1: ")








if __name__ == '__main__':
    main()