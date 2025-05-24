class Mancala:
    def __init__(self):
        self.board = self.createBoard()

    def createBoard(self):
        # spots 0 through 5 and 7 through 12 contain marbles. Player 0 is 0 through 5 and player 1 is 7-12
        # 6 and 13 are the mancalas. The mancala at index 6 belongs to player 0, and 13 belongs to 1
        board = [4] * 14
        board[6] = 0
        board[13] = 0
        return board
    
    # Returns two values: first is if the game is over and second is if the current player get another turn
    def turn(self, player, selection):
        # TBD: will both players give selection 1-6, and we convert based on which player it is?
        if (selection == 6 or selection == 13) \
            or (player == 0 and (selection > 5 or selection < 0)) \
            or (player == 1 and (selection < 5 or selection > 13)) \
            or self.board[selection] == 0:
            # invalid selection
            raise Exception ("Invalid selection. Try again.") # TODO: custom exception
        
        marbles = self.board[selection]
        self.board[selection] = 0

        current_hole = selection
        while marbles > 0:
            # iterate current hole, looping around after 13
            if current_hole == 13:
                current_hole = 0
            else: current_hole += 1

            # make sure it's not other player's mancala
            if (player == 0 and current_hole == 13) or (player == 1 and current_hole == 6):
                current_hole += 1

            # drop marble into hole
            self.board[current_hole] += 1
            marbles -= 1
        
        if self.checkGameOver() == True:
            return True, False
        
        # One more turn
        if current_hole == 6 or current_hole == 13:
            return False, True
        
        else: return False, False
    
    def checkGameOver(self):
        player0_marbles = sum(self.board[0:6])
        player1_marbles = sum(self.board[7:13])

        if player1_marbles == 0 or player1_marbles == 0:
            return True

        return False



    # TODO: maybe have an alternate view for the other player so that it feels like they're looking at the board from their POV
    def printBoard(self):
        print("        -- Player 2 --")
        print("  ", end="")
        for i in range(12, 6, -1):
            print(f" {self.board[i]:2}", end=" ")
        print()
        print(f"{self.board[13]:2}                        {self.board[6]:2}")
        print("  ", end="")
        for i in range(0, 6):
            print(f" {self.board[i]:2}", end=" ")
        print("\n        -- Player 1 --")

            
                
