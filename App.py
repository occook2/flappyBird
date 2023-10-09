import os, neat, visualize
import Game, Bird

def main():
    # Main entry point into the entire application
    # The main purpose of this application is for an AI to be able to play 
    # Flappy Bird through trial and error. This should run the trials
    
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)

def run(config_file):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, \
                         neat.DefaultStagnation, config_file)
    
    # Create Population
    pop = neat.Population(config)

    # Optional - Show detailed statistics about each generation of Birds
    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)

    game = Game.Game()
    winner = pop.run(play, 50)

def play(genomes, config):
    game = Game.Game()
    game.play(genomes, config)

if __name__ == "__main__":
    main()

