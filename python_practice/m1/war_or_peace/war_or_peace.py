import turn, player, deck, card
def main():
    player1 = input('Enter Player 1 name: ')
    player2 = input('Enter Player 2 name: ')
    start = input(
        f"Welcome to War! (or Peace) This game will be played with 52 cards.\nThe players today are {player1} and {player2}.\nType 'GO' to start the game! ").upper()
    if start == 'GO':
        print(new_game())

def new_game():
    ...

if __name__ == '__main__':
    main()