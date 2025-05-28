import copy

class Mancala:
    def __init__(self):
        self.board = self.createBoard()

    def createBoard(self):
        # spots 0 through 5 and 7 through 12 contain marbles; 6 & 13 are the stores
        board = [4] * 14
        board[6] = 0
        board[13] = 0
        return board

    def _is_valid_move(self, player, selection):
        # Disallow selecting stores or opponent pits or empty pits
        if selection in (6, 13):
            return False
        if player == 0 and not (0 <= selection <= 5):
            return False
        if player == 1 and not (7 <= selection <= 12):
            return False
        if self.board[selection] == 0:
            return False
        return True

    def _execute_move(self, board, player, selection):
        """
        Perform the marble distribution and capture logic.
        Returns True if the player gets another turn, else False.
        """
        marbles = board[selection]
        board[selection] = 0
        current = selection

        # Distribute marbles
        while marbles > 0:
            current = (current + 1) % 14
            # Skip opponent's store
            if (player == 0 and current == 13) or (player == 1 and current == 6):
                continue
            board[current] += 1
            marbles -= 1

        # Extra turn if last marble lands in player's store
        if (player == 0 and current == 6) or (player == 1 and current == 13):
            return True

        # Capture rule: last in empty own pit
        own_range = range(0, 6) if player == 0 else range(7, 13)
        store_index = 6 if player == 0 else 13
        if current in own_range and board[current] == 1:
            opp = 12 - current
            if board[opp] > 0:
                board[store_index] += board[opp] + 1
                board[opp] = 0
                board[current] = 0

        return False

    def turn(self, player, selection):
        """
        Apply a turn on the main board. Returns (game_over, extra_turn).
        """
        if not self._is_valid_move(player, selection):
            raise Exception("Invalid selection. Try again.")

        extra = self._execute_move(self.board, player, selection)

        # Check end condition
        game_over = self.checkGameOver(self.board)
        return (True, False) if game_over else (False, extra)

    def simulate_turn(self, board, player, selection):
        """
        Simulate a turn on a copied board for Minimax. Returns (new_board, game_over, next_player).
        """
        temp = copy.deepcopy(board)
        extra = self._execute_move(temp, player, selection)
        game_over = self.checkGameOver(temp)
        next_player = player if extra else 1 - player
        return temp, game_over, next_player

    def checkGameOver(self, board=None):
        """
        Returns True if either side's pits are empty.
        """
        b = board if board is not None else self.board
        return sum(b[0:6]) == 0 or sum(b[7:13]) == 0

    def getScores(self):
        player0_score = sum(self.board[0:7])
        player1_score = sum(self.board[7:14])
        return player0_score, player1_score

    def printBoard(self):
        # TODO: (maybe) make this wait a couple seconds
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

# Minimax and helpers outside the class

def get_legal_moves(board, player):
    if player == 0:
        return [i for i in range(0, 6) if board[i] > 0]
    return [i for i in range(7, 13) if board[i] > 0]


def evaluate_board(board, player):
    # Simple store-difference heuristic
    return board[6] - board[13] if player == 0 else board[13] - board[6]


def minimax(board, depth, player, maximizing_player):
    # Terminal or depth limit
    if depth == 0 or sum(board[0:6]) == 0 or sum(board[7:13]) == 0:
        return evaluate_board(board, maximizing_player), None

    moves = get_legal_moves(board, player)
    if not moves:
        return evaluate_board(board, maximizing_player), None

    best_move = None
    if player == maximizing_player:
        best_val = float('-inf')
        for m in moves:
            new_b, over, next_p = Mancala().simulate_turn(board, player, m)
            val, _ = minimax(new_b, depth-1, next_p, maximizing_player)
            if val > best_val:
                best_val, best_move = val, m
        return best_val, best_move
    else:
        best_val = float('inf')
        for m in moves:
            new_b, over, next_p = Mancala().simulate_turn(board, player, m)
            val, _ = minimax(new_b, depth-1, next_p, maximizing_player)
            if val < best_val:
                best_val, best_move = val, m
        return best_val, best_move
