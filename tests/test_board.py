from src.board import Board
from testfixtures import compare

def test_print_board(capsys):
    
    # Arrange
    expected = \
'''\

##############################
  ###     CONNECT - 4    ###
##############################
  _   _   _   _   _   _   _
  1   2   3   4   5   6   7
#############################
|   |   |   |   |   |   |   | 
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
#############################

'''
    
    # Act
    Board().print_board()
    captured = capsys.readouterr()
    
    # Assert
    compare(captured.out, expected, trailing_whitespace=False)


def test_check_state():
    # Arrange
    b = Board()

    # Act
    b.insert_piece('X', 0, 0)
    b.insert_piece('X', 0, 1)
    b.insert_piece('X', 0, 2)
    b.insert_piece('X', 0, 3)
    test_check_state = b.check_state('X')

    # Assert
    assert test_check_state == True


def test_insert_piece():
    # Arrange
    b = Board()
    test_piece = 'X'
    test_row = 2
    test_column = 5

    # Act
    b.insert_piece(test_piece, test_row, test_column)

    # Assert
    assert b.board[test_row][test_column] == test_piece


def test_is_valid():
    # Arrange
    b = Board()

    # Act
    test_state = b.is_valid(4)

    # Assert
    assert test_state == True


def test_get_next_row():
    # Arrange
    b = Board()

    # Act
    text_next_row = b.get_next_row(3)

    # Assert
    assert text_next_row == 5


def test_board_full():
    # Arrange
    b = Board()

    # Act
    b.insert_piece('X', 0, 0)
    b.insert_piece('X', 0, 1)
    b.insert_piece('X', 0, 2)
    b.insert_piece('X', 0, 3)
    b.insert_piece('X', 0, 4)
    b.insert_piece('X', 0, 5)
    b.insert_piece('X', 0, 6)
    test_full_board = b.board_full()

    # Assert
    assert test_full_board == True


def test_is_terminal_node():
    # Arrange
    b = Board()
    b.insert_piece('X', 0, 0)
    b.insert_piece('X', 0, 1)
    b.insert_piece('X', 0, 2)
    b.insert_piece('X', 0, 3)

    # Act
    test_player_state = b.check_state('X')
    test_ai_state = b.check_state('O')
    test_get_valid_location = b.get_valid_locations()

    # Assert
    assert test_player_state or test_ai_state or len(test_get_valid_location) == 0


def test_get_valid_locations():
    # Arrange
    b = Board()

    # Act
    test_valid_locations = b.get_valid_locations()

    # Assert
    assert test_valid_locations == [0, 1, 2, 3, 4, 5, 6]


def test_score_position():
    # Arrange
    b = Board()

    # Act
    b.insert_piece('X', 0, 2)
    b.insert_piece('X', 1, 2)
    b.insert_piece('X', 2, 2)

    test_score = b.score_position('X')

    # Assert
    assert test_score == 7

def test_evaluate_window():
    # Arrange
    b = Board()

    # Act
    b.insert_piece('X', 0, 5)
    b.insert_piece('X', 1, 2)
    b.insert_piece('X', 2, 1)

    test_score = b.score_position('X')

    # Assert
    assert test_score == 2