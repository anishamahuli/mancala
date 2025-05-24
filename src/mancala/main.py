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



if __name__ == "__main__":
    main()