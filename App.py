import Game, Bird

def main():
    # Main entry point into the entire application
    # The main purpose of this application is for an AI to be able to play 
    # Flappy Bird through trial and error. This should run the trials
    
    birds = [Bird.Bird()]
    game = Game.Game(birds, 0)
    game.play()

if __name__ == "__main__":
    main()