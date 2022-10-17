try:
    from src.game import Game
except ModuleNotFoundError:
    from game import Game
    
def main():
    
    # Create game instance
    game = Game()
    game.launch_menu()

    # Main game loop
    game.loop()


if __name__ == '__main__':
    main()
