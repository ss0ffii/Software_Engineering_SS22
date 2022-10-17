try:
    from src.board import Board
    from src.players import Human, AI_Player
except ModuleNotFoundError:
    from board import Board
    from players import Human, AI_Player

import os
import time
import sys
import shelve
from pathlib import Path

MODES = ['Player vs. Player', 'Player vs. Computer', 'Computer vs. Computer']
DIFFICULTIES = ['Easy', 'Medium', 'Hard']

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
class Game:
    """ Class used to handle game logic.
    
    Attributes
    ----------
    game_mode : int
        Chosen mode of play
    p1 : Player
        Player 1    
    p2 : Player
        Player 2
    board : Board
        Game board 
    win : bool
        Current state of game    
    """

    def __init__(self) -> None:
        self.game_mode = None
        self.p1 = None
        self.p2 = None
        self.board = Board()
        self.win = False

    def launch_menu(self) -> None:
        print("Welcome to Connect Four!\n")
        print("New Game  [0] \n"
              "Load Game [1] \n")
        choice = None
        while choice not in [0, 1]:
            choice = int(input("Enter your choice [0-1]: "))

        if choice == 0:
            self.choose_gamemode()
            self.setup_players()
        else:
            self.load_game()

    def choose_gamemode(self) -> None:
        print(f"\nPlease choose game mode: \n"
              f"1. {MODES[0]} \n"
              f"2. {MODES[1]} \n"
              f"3. {MODES[2]} \n")

        while self.game_mode not in [1, 2, 3]:
            self.game_mode = int(input("Enter your choice [1-3]: "))

        print(f"{MODES[self.game_mode - 1]} mode selected. \n")
        
    def choose_difficulty(self, number: str) -> None:
        difficulty = 0

        print(f"Please choose Computer{number} difficulty: \n"
              f"1. {DIFFICULTIES[0]} \n"
              f"2. {DIFFICULTIES[1]} \n"
              f"3. {DIFFICULTIES[2]} \n")

        while difficulty not in [1, 2, 3]:
            difficulty = int(input("Enter your choice [1-3]: "))

        print(f"{DIFFICULTIES[difficulty - 1]} mode for Computer{number} selected.\n")

        return difficulty
    
    def setup_players(self) -> None:
        if self.game_mode == 1: # Player vs. Player
            self.p1 = Human(1)
            self.p2 = Human(2)

        if self.game_mode == 2: # Player vs. Computer
            diff = self.choose_difficulty("")
            self.p1 = Human(1)
            self.p2 = AI_Player(2, diff)

        if self.game_mode == 3: # Computer vs. Computer
            diff = self.choose_difficulty(" 1")
            self.p1 = AI_Player(1, diff)

            diff = self.choose_difficulty(" 2")
            self.p2 = AI_Player(2, diff)

            self.p1.piece = 'X'
        
        while self.p1.piece not in ['X', 'O']:
            self.p1.piece = str(input('Player 1, choose X or O: '))

        if self.p1.piece == 'X':
            self.p2.piece = 'O'
        else:
            self.p2.piece = 'X'
        
        print(f"Player 1 is {self.p1.piece}.")
        print(f"Player 2 is {self.p2.piece}.")

        self.countdown()
        
    def countdown(self) -> None:
        print("\nGet ready! ", end = '')
        for remaining in range(3, 0, -1):
            print(f"{remaining}... ", end='')
            time.sleep(1)
            
    def loop(self) -> None:
        cls()
        self.board.print_board()
        while not self.win:
            for player in [self.p1, self.p2]:
                print(
                    f'Menu: Type \'quit\' to exit the game, \'save\' to save current progress, or \'load\' to load a previously saved game.')
                while True:
                    # Check if the board is already full
                    if self.board.board_full():
                        self.game_over()
                    action = player.action(self.board)
                    column = None

                    if isinstance(action, str):
                        self.select_options(action)
                    elif isinstance(action, int):
                        column = action
                        row = self.board.get_next_row(column)

                        # print(row, column)
                        if self.board.is_valid(column):
                            self.board.insert_piece(player.piece, row, column)
                            break
                        print("Invalid move, try again...")
                cls()
                self.board.print_board()
                self.win = self.board.check_state(player.piece)

                if self.win:
                    print(f"Player {player.number} wins!")
                    self.game_over()

    def select_options(self, action: str) -> None:
        if action == 'load':
            self.load_game()
            self.board.print_board()

        if action == 'save':
            self.save_game()

        if action == 'quit':
            self.quit_game()

    def quit_game(self) -> None:
        while True:
            inp = input("Save progress before quitting? [y/n]: ").lower()

            if inp in ['y', 'n']:
                if inp == 'y':
                    self.save_game()
                break
            else:
                print("Invalid input, try again...")

        print("Thanks for playing! Until next time.")
        sys.exit()

    def save_game(self) -> None:
        save_path = Path(sys.argv[0]).parent.parent / Path('data/save')
        save_file = shelve.open(fr'{save_path}')

        save_file['board'] = self.board
        save_file['game_mode'] = self.game_mode
        save_file['player_one'] = self.p1
        save_file['player_two'] = self.p2

        save_file.close()

        print("File saved.")

    def load_game(self) -> None:

        save_path = Path(sys.argv[0]).parent.parent / Path('data/save')
        save_file = shelve.open(fr'{save_path}')

        self.game_mode = save_file['game_mode']
        self.board = save_file['board']

        self.p1 = save_file['player_one']
        self.p2 = save_file['player_two']

        print("File loaded.")

    def game_over(self) -> None:
        print("Game over!")
        while True:
            inp = str(input("Play again? [y/n]: ").lower())

            if inp in ['y', 'n']:
                if inp == 'y':
                    self.restart_game()
                    break
                else:
                    print("Thanks for playing! Until next time.")
                    sys.exit()
            else:
                print("Invalid input, try again...")

    def restart_game(self) -> None:
        # Clear board and reset game state
        self.board = Board()
        self.win = False

        self.board.print_board()
