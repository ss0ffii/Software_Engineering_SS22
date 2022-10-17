Feature: Human Gameplay of Connect Four
    Human Player plays Connect Four against Human Player
    Scenario: player (X) wins
          Given Game start
          And Beginning of the game
          When The game mode 1 is chosen
          And player selected a piece X
          And Player 1 makes a move 1
          And Player 2 makes a move 2
          And Player 1 makes a move 1
          And Player 2 makes a move 3
          And Player 1 makes a move 1
          And Player 2 makes a move 1
          And Player 1 makes a move 2
          And Player 2 makes a move 4
          And Player 1 makes a move 5
          And Player 2 makes a move 3
          And Player 1 makes a move 3
          And Player 2 makes a move 4
          And Player 1 makes a move 5
          And Player 2 makes a move 4
          And Player 1 makes a move 4
          Then Player 1 wins!

    Scenario: player (X) wins
          Given Game start
          And Beginning of the game
          When The game mode 1 is chosen
          And player selected a piece X
          And Player 1 makes a move 1
          And Player 2 makes a move 3
          And Player 1 makes a move 2
          And Player 2 makes a move 3
          And Player 1 makes a move 3
          And Player 2 makes a move 4
          And Player 1 makes a move 2
          And Player 2 makes a move 5
          And Player 1 makes a move 6
          And Player 2 makes a move 5
          And Player 1 makes a move 4
          And Player 2 makes a move 4
          And Player 1 makes a move 4
          Then Player 1 wins!

    Scenario: player (O) wins
          Given Game start
          And Beginning of the game
          When The game mode 1 is chosen
          And player selected a piece X
          And Player 1 makes a move 3
          And Player 2 makes a move 5
          And Player 1 makes a move 1
          And Player 2 makes a move 4
          And Player 1 makes a move 7
          And Player 2 makes a move 6
          And Player 1 makes a move 1
          And Player 2 makes a move 5
          And Player 1 makes a move 2
          And Player 2 makes a move 6
          And Player 1 makes a move 4
          And Player 2 makes a move 6
          And Player 1 makes a move 6
          And Player 2 makes a move 5
          And Player 1 makes a move 5
          And Player 2 makes a move 4
          And Player 1 makes a move 3
          And Player 2 makes a move 3
          Then Player 2 wins!

    Scenario: player (O) wins
          Given Game start
          And Beginning of the game
          When The game mode 1 is chosen
          And player selected a piece X
          And Player 1 makes a move 1
          And Player 2 makes a move 3
          And Player 1 makes a move 1
          And Player 2 makes a move 5
          And Player 1 makes a move 4
          And Player 2 makes a move 1
          And Player 1 makes a move 3
          And Player 2 makes a move 2
          And Player 1 makes a move 4
          And Player 2 makes a move 2
          And Player 1 makes a move 1
          And Player 2 makes a move 2
          And Player 1 makes a move 2
          And Player 2 makes a move 3
          And Player 1 makes a move 4
          And Player 2 makes a move 4
          And Player 1 makes a move 7
          And Player 2 makes a move 5
          And Player 1 makes a move 7
          And Player 2 makes a move 5
          And Player 1 makes a move 5
          And Player 2 makes a move 5
          Then Player 2 wins!