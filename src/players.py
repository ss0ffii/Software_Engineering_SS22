try:
    from src.board import Board
except ModuleNotFoundError:
    from board import Board
    
import random
import math
import copy
import time

DIGITS1TO7 = '1 2 3 4 5 6 7'.split()

class Player():
    """ Generic player class.
    
    Attributes
    ----------
    number : int
        Indicates if player 1 or 2
    piece : str
        Indicates player-selected board piece (X/O)    
    """   
    
    def __init__(self, number: int) -> None:
        self.number = number
        self.piece = None

    def action(self):
        pass

    def set_player(self, player):
        self.number = player.number
        self.piece = player.piece


class Human(Player):
    def __init__(self, number: int) -> None:
        super().__init__(number)

    def action(self, board: Board) -> int:
        while True:
            action = input(f'Player {self.number}, enter your move [1-7]: ').lower()
            if action in ['save', 'load', 'quit']:
                return action
            elif action in DIGITS1TO7:
                return int(action) - 1
            else:
                print("Invalid input, try again...")

class AI_Player(Player):
    def __init__(self, number: int, difficulty: int) -> None:
        super().__init__(number)
        self.difficulty = difficulty

    def action(self, board: Board) -> int:
        if self.difficulty == 1:
            action = self.pick_best_move(board) # Dumber algorithm
        else:
            action = self.minimax(board, self.difficulty + 2, -math.inf, math.inf, True)[0] # Decrease initial depth for easier difficulty
        
        print(f"Computer {self.number} move: {int(action) + 1}")

        time.sleep(0.8)

        return int(action)
                
    def minimax(self, board: Board, depth: int, alpha: int, beta: int, maximizing_player: bool):
        ai_piece = self.piece
        player_piece = 'X'
        if ai_piece == 'X':
            player_piece = 'O'

        valid_locations = board.get_valid_locations()
        is_terminal = board.is_terminal_node(ai_piece)

        if depth == 0 or is_terminal:
            if is_terminal:
                if board.check_state(ai_piece): # AI wins with next move
                    return (None, 100000000000000)
                elif board.check_state(player_piece):
                    return (None, -10000000000000)
                else:  # Game is over, no more valid moves
                    return (None, 0)
            else:  # Depth is zero
                return (None, board.score_position(ai_piece))

        if maximizing_player:
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = board.get_next_row(col)
                b_copy = copy.deepcopy(board)
                b_copy.insert_piece(ai_piece, row, col)
                new_score = self.minimax(
                    b_copy, depth-1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value
        else:  # Minimizing player
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = board.get_next_row(col)
                b_copy = copy.deepcopy(board)
                b_copy.insert_piece(player_piece, row, col)
                new_score = self.minimax(b_copy, depth-1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value

    def pick_best_move(self, board: Board) -> int:
        valid_locations = board.get_valid_locations()
        best_score = -10000
        best_col = random.choice(valid_locations)

        for col in valid_locations:
            row = board.get_next_row(col)
            temp_board = copy.deepcopy(board)
            temp_board.insert_piece(self.piece, row, col)
            score = temp_board.score_position(self.piece)
            if score > best_score:
                best_score = score
                best_col = col

        return best_col
