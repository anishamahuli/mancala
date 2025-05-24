from mancala import Mancala
    
def main():
    game = Mancala()
    game_over = False
    player0 = True

    while not game_over:
        game.printBoard()
        if player0: curr_player = 0
        else: curr_player = 1
        # prompt player for selection

        # TODO: make hole selection more intuitive for the players (not zero-indexed)
        selection = int(input(f"Player {curr_player}: Please select which pocket you would like to play. "))
        
        game_over, go_again = game.turn(curr_player, selection)
        if go_again:
            print("Player ", curr_player, ", you get another turn.")
            continue

        player0 = not player0

    player0_score, player1_score = game.getScores()
    if player0_score > player1_score:
        print("Player 0 wins ", player0_score," to ", player1_score)
    elif player1_score > player0_score:
        print("Player 1 wins ", player1_score," to ", player0_score)
    else:
        print("It's a draw. Good game!")

if __name__ == "__main__":
    main()