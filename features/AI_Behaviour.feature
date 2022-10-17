Feature: AI Gameplay of Connect Four
    Player plays Connect Four (against Computer)
    Scenario: player (X) wins
        Given The game starts
        And New game is started
        When The game mode 2 is chosen 
        And player chooses a piece X
        And Player 1 chooses column 1
        And Player 2 chooses column 5
        And Player 1 chooses column 4
        And Player 2 chooses column 3
        And Player 1 chooses column 3
        And Player 2 chooses column 5
        And Player 1 chooses column 2
        And Player 2 chooses column 3
        And Player 1 chooses column 4
        And Player 2 chooses column 2
        And Player 1 chooses column 4
        And Player 2 chooses column 7
        And Player 1 chooses column 4
        Then Player 1 wins 


    Scenario: player (X) wins
        Given The game starts
        And New game is started
        When The game mode 2 is chosen 
        And player chooses a piece X
        And Player 1 chooses column 7
        And Player 2 chooses column 3
        And Player 1 chooses column 6
        And Player 2 chooses column 5
        And Player 1 chooses column 2
        And Player 2 chooses column 3
        And Player 1 chooses column 1
        And Player 2 chooses column 3
        And Player 1 chooses column 7
        And Player 2 chooses column 3
        Then Player 1 wins 


    Scenario: Computer (O) wins
        Given The game starts
        And New game is started
        When The game mode 2 is chosen 
        And player chooses a piece X
        And Player 1 chooses column 3
        And Player 2 chooses column 4
        And Player 1 chooses column 4
        And Player 2 chooses column 4
        And Player 1 chooses column 5
        And Player 2 chooses column 4
        And Player 1 chooses column 5
        And Player 2 chooses column 5
        And Player 1 chooses column 3
        And Player 2 chooses column 3
        And Player 1 chooses column 2
        And Player 2 chooses column 2
        And Player 1 chooses column 1
        And Player 2 chooses column 2      
        Then Player 2 wins 


    Scenario: Computer (O) wins
        Given The game starts
        And New game is started
        When The game mode 2 is chosen 
        And player chooses a piece X
        And Player 1 chooses column 7
        And Player 2 chooses column 4
        And Player 1 chooses column 5
        And Player 2 chooses column 4
        And Player 1 chooses column 4
        And Player 2 chooses column 4
        And Player 1 chooses column 5
        And Player 2 chooses column 4
        And Player 1 chooses column 5
        And Player 2 chooses column 5
        And Player 1 chooses column 6
        And Player 2 chooses column 5
        And Player 1 chooses column 6
        And Player 2 chooses column 6
        And Player 1 chooses column 3
        And Player 2 chooses column 4
        And Player 1 chooses column 3
        And Player 2 chooses column 1
        And Player 1 chooses column 7
        And Player 2 chooses column 6
        And Player 1 chooses column 7
        And Player 2 chooses column 7 
        Then Player 2 wins 