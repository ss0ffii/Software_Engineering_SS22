COLUMN_COUNT = 7
ROW_COUNT = 6
WINDOW_LENGTH = 4
EMPTY = ' '
PIECE_X = 'X'
PIECE_O = 'O'

class Board:
    """ Class used to handle board-related logic.
    
    Attributes
    ----------
    head : str
        Header of board
    line : str
        Line seperating elements
    top : str
        Visual indicator of where to place a piece
    numbers : str
        Numeric indicator of where to place a piece
    board : list of lists of ints
        Nested list representation of board
        Outer elements rows, inner elements columns    
    """

    def __init__(self) -> None:
        self.head = '''##############################\n  ###     CONNECT - 4    ###\n##############################'''
        self.line = '#############################'
        self.top = '  _   _   _   _   _   _   _ '
        self.numbers = '  1   2   3   4   5   6   7 '
        self.board = [[] for _ in range(ROW_COUNT)]
        
        for row in self.board:
            for _ in range(COLUMN_COUNT):
                row.append(' ')

    def print_board(self) -> None:
        # for index, row in enumerate(self.board):
        #     print(index, row)
        print()
        print(self.head)
        print(self.top)
        print(self.numbers)        
        print(self.line)
       
        self.row = [[] for _ in range(ROW_COUNT)]
        
        for i in range(ROW_COUNT):
           self.row[i] = '| '

        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                self.row[row] += str(self.board[row][column]) + ' | '
            print(self.row[row])
        print(self.line)
        print('')

    def check_state(self, piece: str) -> bool:
                    
        # Check horizontal
        for column in range(COLUMN_COUNT - 3):
            for row in range(ROW_COUNT):
                if self.board[row][column] == piece and self.board[row][column + 1] == piece and self.board[row][column + 2] == piece and \
                        self.board[row][column + 3] == piece:
                    return True
        # Check vertical
        for column in range(COLUMN_COUNT):
            for row in range(ROW_COUNT - 3):
                if self.board[row][column] == piece and self.board[row + 1][column] == piece and self.board[row + 2][column] == piece and \
                        self.board[row + 3][column] == piece:
                    return True
        # Check diagonal upwards
        for column in range(COLUMN_COUNT - 3):
            for row in range(ROW_COUNT - 3):
                if self.board[row][column] == piece and self.board[row + 1][column + 1] == piece and \
                        self.board[row + 2][column + 2] == piece and self.board[row + 3][column + 3] == piece:
                    return True
        # Check diagonal downwards
        for column in range(COLUMN_COUNT - 3):
            for row in range(3, ROW_COUNT):
                if self.board[row][column] == piece and self.board[row - 1][column + 1] == piece and \
                        self.board[row - 2][column + 2] == piece and self.board[row - 3][column + 3] == piece:
                    return True
        
        # return False
    
    def insert_piece(self, piece: str, row: int, column: int) -> None:
        self.board[row][column] = piece
    
    def is_valid(self, column: int) -> bool:
        return self.board[0][column] == EMPTY
    
    def get_next_row(self, column: int) -> int:
        """ Finds next available smallest row to place a piece.
        """
        for r in range(ROW_COUNT - 1, -1, -1):
            if self.board[r][column] == EMPTY:
                return r

    def board_full(self) -> bool:
        counter = 0
        for i in range(COLUMN_COUNT):
            if self.board[0][i] != EMPTY:
                counter += 1
        if counter > 6:
            return True
    
    def is_terminal_node(self, ai_piece: str) -> bool:
        """ Checks if current state results in a win or a draw.
        """
        player_piece = PIECE_X
        if ai_piece == PIECE_X:
            player_piece = PIECE_O

        return self.check_state(player_piece) or self.check_state(ai_piece) or len(self.get_valid_locations()) == 0

    def get_valid_locations(self):
        valid_locations = []
        for col in range(COLUMN_COUNT):
            if self.is_valid(col):
                valid_locations.append(col)
        return valid_locations

    def score_position(self, piece: str) -> int:
        """ Assigns a score for where to insert a piece based on the position's "value".
        """
        score = 0

        ## Score center column
        center_array = []
        for row in self.board:
            center_array.append(row[COLUMN_COUNT//2])
        center_count = center_array.count(piece)
        score += center_count * 3

        ## Score Horizontal
        for r in range(ROW_COUNT):
            row_array = self.board[r]
            for c in range(COLUMN_COUNT-3):
                window = row_array[c:c+WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        ## Score Vertical
        for c in range(COLUMN_COUNT):
            col_array = []
            for row in self.board:
                col_array.append(row[c])
            for r in range(ROW_COUNT-3):
                window = col_array[r:r+WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        ## Score posiive sloped diagonal
        for r in range(ROW_COUNT-3):
            for c in range(COLUMN_COUNT-3):
                window = [self.board[r+i][c+i] for i in range(WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        for r in range(ROW_COUNT-3):
            for c in range(COLUMN_COUNT-3):
                window = [self.board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        return score

    def evaluate_window(self, window: list, piece: str) -> int:
        """ Calculates score based on the pieces in a range of locations. 
        """
        score = 0
        opp_piece = PIECE_X
        if piece == PIECE_X:
            opp_piece = PIECE_O

        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(EMPTY) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(EMPTY) == 2:
            score += 2

        if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
            score -= 4

        return score
