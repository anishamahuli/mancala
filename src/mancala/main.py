from mancala import Mancala, minimax

def get_human_move(board, player):
    while True:
        try:
            selection = int(input(f"Player {player+1}, select a pocket (1-6): "))
            if player == 0:
                index = selection - 1
            else:
                index = selection + 6
            if board[index] == 0:
                print("That pocket is empty. Try again.")
                continue
            return index
        except (ValueError, IndexError):
            print("Invalid input. Try again.")

def get_cpu_move(board, player, depth=5):
    _, move = minimax(board, depth, player, player)
    print(f"CPU Player {player+1} chooses pocket {(move - 6) if player == 1 else (move + 1)}")
    return move

def main():
    game = Mancala()

    # Choose player types: 'h' = human, 'c' = cpu
    player_types = {}
    for i in [0, 1]:
        p_type = input(f"Is Player {i+1} a human or cpu? (h/c): ").lower()
        player_types[i] = 'cpu' if p_type == 'c' else 'human'

    current_player = 0
    game_over = False

    while not game_over:
        game.printBoard()
        board = game.board

        if player_types[current_player] == 'cpu':
            selection = get_cpu_move(board, current_player)
        else:
            selection = get_human_move(board, current_player)

        try:
            game_over, go_again = game.turn(current_player, selection)
        except Exception as e:
            print(e)
            continue

        if go_again:
            print(f"Player {current_player+1} gets another turn!")
            continue

        current_player = 1 - current_player  # switch player

    # Game ended
    print("\nGame over! Final board:")
    game.printBoard()
    player0_score, player1_score = game.getScores()

    print(f"Player 1 score: {player0_score}")
    print(f"Player 2 score: {player1_score}")
    if player0_score > player1_score:
        print("Player 0 wins!")
    elif player1_score > player0_score:
        print("Player 1 wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
