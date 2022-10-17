Feature: Saving function for Connect Four

  Scenario: Type 'save' while playing a game
    Given Player 1 starts the game
    When Player 1 is prompted to enter their choice
    And Player 1 chooses a new game (0)
    And Player 1 chooses to play against another player (1)
    And Player 1 chooses (X)
    And Player 1 places their piece in column (2)
    And Player 2 places their piece in column (3)
    And Player 1 places their piece in column (2)
    And Player 2 places their piece in column (3)
    And Player 1 types (save)
    Then The current progress is saved