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
        new_game()

def new_game():
    random.shuffle(all_cards)
    half = len(all_cards) // 2
    deck1 = deck.Deck(all_cards[:half])
    deck2 = deck.Deck(all_cards[half:])
    player1 = player.Player('Loki', deck1)
    player2 = player.Player('Karl', deck2)

    turn_count = 0
    while not player1.has_lost() and not player2.has_lost():
        turn_count += 1
        game = turn.Turn(player1, player2)
        turn_type = game.type()
        winner = game.winner()

        if turn_type == 'mutually_assured_destruction':
            game.pile_cards()
            print(f"Turn {turn_count}: *mutually assured destruction* 6 cards removed from play")
        else:
            game.pile_cards()
            game.award_spoils(winner)
            if turn_type == 'war':
                print(f"Turn {turn_count}: WAR - {winner.name} won {len(game.spoils_of_war)} cards")
            else:
                print(f"Turn {turn_count}: {winner.name} won {len(game.spoils_of_war)} cards")

        if turn_count >= 1000000:
            print("---- DRAW ----")
            break

    if player1.has_lost():
        print(f"*~*~*~* {player2.name} has won the game! *~*~*~*")
    elif player2.has_lost():
        print(f"*~*~*~* {player1.name} has won the game! *~*~*~*")


if __name__ == '__main__':
    main()