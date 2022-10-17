Feature: AI vs AI Gameplay of Connect Four
    Computer plays Connect Four (against Computer)
    Scenario: Computer 1 (X) wins
        Given Start the programm 
        And New game starts
        When The game mode 3 is chosen
        And for Computer 1 is chosen level of difficulty 1
        And for Computer 2 is chosen level of difficulty 1
        And Computer 1 chooses column 4
        And Computer 2 chooses column 4
        And Computer 1 chooses column 3
        And Computer 2 chooses column 3
        And Computer 1 chooses column 2
        And Computer 2 chooses column 4
        And Computer 1 chooses column 5 
        Then Computer 1 wins 


    Scenario: Computer 1 (X) wins
        Given Start the programm 
        And New game starts
        When The game mode 3 is chosen
        And for Computer 1 is chosen level of difficulty 2
        And for Computer 2 is chosen level of difficulty 2
        And Computer 1 chooses column 4
        And Computer 2 chooses column 3
        And Computer 1 chooses column 3
        And Computer 2 chooses column 4
        And Computer 1 chooses column 3
        And Computer 2 chooses column 3
        And Computer 1 chooses column 4
        And Computer 2 chooses column 3
        And Computer 1 chooses column 4
        And Computer 2 chooses column 4
        And Computer 1 chooses column 4
        And Computer 2 chooses column 1
        And Computer 1 chooses column 3
        And Computer 2 chooses column 7
        And Computer 1 chooses column 2
        And Computer 2 chooses column 7
        And Computer 1 chooses column 7
        And Computer 2 chooses column 7
        And Computer 1 chooses column 1
        And Computer 2 chooses column 1
        And Computer 1 chooses column 1
        And Computer 2 chooses column 1
        And Computer 1 chooses column 7
        And Computer 2 chooses column 6
        And Computer 1 chooses column 5
        And Computer 2 chooses column 5
        And Computer 1 chooses column 6
        And Computer 2 chooses column 6
        And Computer 1 chooses column 6
        And Computer 2 chooses column 2
        And Computer 1 chooses column 2
        Then Computer 1 wins

    
    Scenario: Computer 1 (X) wins
        Given Start the programm 
        And New game starts
        When The game mode 3 is chosen
        And for Computer 1 is chosen level of difficulty 3
        And for Computer 2 is chosen level of difficulty 3
        And Computer 1 chooses column 4
        And Computer 2 chooses column 4
        And Computer 1 chooses column 4
        And Computer 2 chooses column 3
        And Computer 1 chooses column 4
        And Computer 2 chooses column 3
        And Computer 1 chooses column 3
        And Computer 2 chooses column 4
        And Computer 1 chooses column 3
        And Computer 2 chooses column 4
        And Computer 1 chooses column 6
        And Computer 2 chooses column 7
        And Computer 1 chooses column 3
        And Computer 2 chooses column 3
        And Computer 1 chooses column 6
        And Computer 2 chooses column 1
        And Computer 1 chooses column 1
        And Computer 2 chooses column 1
        And Computer 1 chooses column 1
        And Computer 2 chooses column 1
        And Computer 1 chooses column 1
        And Computer 2 chooses column 2
        And Computer 1 chooses column 2
        And Computer 2 chooses column 2
        And Computer 1 chooses column 2
        Then Computer 1 wins


    Scenario: Computer 2 (O) wins
        Given Start the programm 
        And New game starts
        When The game mode 3 is chosen
        And for Computer 1 is chosen level of difficulty 1
        And for Computer 2 is chosen level of difficulty 3
        And Computer 1 chooses column 4
        And Computer 2 chooses column 4
        And Computer 1 chooses column 3
        And Computer 2 chooses column 5
        And Computer 1 chooses column 3
        And Computer 2 chooses column 3
        And Computer 1 chooses column 4
        And Computer 2 chooses column 2
        And Computer 1 chooses column 3
        And Computer 2 chooses column 5
        And Computer 1 chooses column 4
        And Computer 2 chooses column 3
        And Computer 1 chooses column 4
        And Computer 2 chooses column 4
        And Computer 1 chooses column 5
        And Computer 2 chooses column 5
        And Computer 1 chooses column 7
        And Computer 2 chooses column 2
        And Computer 1 chooses column 2
        And Computer 2 chooses column 2 
        Then Computer 2 wins


    Scenario: Computer 2 (O) wins
        Given Start the programm 
        And New game starts
        When The game mode 3 is chosen
        And for Computer 1 is chosen level of difficulty 2
        And for Computer 2 is chosen level of difficulty 3
        And Computer 1 chooses column 4
        And Computer 2 chooses column 4
        And Computer 1 chooses column 3
        And Computer 2 chooses column 5
        And Computer 1 chooses column 3
        And Computer 2 chooses column 3
        And Computer 1 chooses column 4
        And Computer 2 chooses column 2
        And Computer 1 chooses column 3
        And Computer 2 chooses column 5
        And Computer 1 chooses column 4
        And Computer 2 chooses column 3
        And Computer 1 chooses column 4
        And Computer 2 chooses column 4
        And Computer 1 chooses column 5
        And Computer 2 chooses column 5
        And Computer 1 chooses column 7
        And Computer 2 chooses column 2
        And Computer 1 chooses column 2
        And Computer 2 chooses column 2
        And Computer 1 chooses column 1
        And Computer 2 chooses column 1
        And Computer 1 chooses column 1
        And Computer 2 chooses column 5
        And Computer 1 chooses column 1
        And Computer 2 chooses column 1
        And Computer 1 chooses column 1
        And Computer 2 chooses column 5
        Then Computer 2 wins