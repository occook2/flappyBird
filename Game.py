import pygame, neat
import Window, Pipe, Ground, Bird

class Game:

    HEIGHT = 800
    WIDTH = 600
    SCROLL_AMOUNT = 5
    FPS = 60

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.window = Window.Window(self.HEIGHT, self.WIDTH)
        self.ground = Ground.Ground()
        self.pipes = []
        self.pipe_clock = 0

        self.birds = []

        self.score = 0

    def play(self, genomes, config):

        nets = []
        ge = []

        for g in genomes:
            net = neat.nn.FeedForwardNetwork(g, config)
            nets.append(net)

            g.fitness = 0
            ge.append(g)

            self.birds.append(Bird.Bird())

        pygame.display.set_caption('BirdBaby.AI')
        pygame.display.flip()

        running = True
        while (running):
            # Update Game Clock
            self.clock.tick(self.FPS)

            # Update Game State
            self.update_game_state()

            # Display Window
            self.window.display(self.birds, self.pipes, self.ground, self.score)
            pygame.display.update()
            
            # Test Collisions 
            for x, bird in enumerate(self.birds):
                for pipe in self.pipes:
                    if self.is_collision(bird, pipe):
                        ge[x].fitness -= 1
                        self.birds.pop(x)
                        nets.pop(x)
                        ge.pop(x)

                    if not pipe.passed and bird.x > pipe.x: # Change Pipe to Passed
                        for g in ge:
                            g.fitness += 5
                        pipe.passed = True
                
                if self.ground_collision(bird):
                    ge[x].fitness -= 1
                    self.birds.pop(x)
                    nets.pop(x)
                    ge.pop(x)

            # Game Event Handler - Will need to connect to AI somehow
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.birds[0].jump()
   
        pygame.quit()
    
    ########## UPDATE GAME STATE HEPER FUNCTIONS ##########
    def update_game_state(self):
        self.update_birds()
        self.update_pipes()
        self.update_ground()

    def update_birds(self):
        for bird in self.birds:
            bird.move()
    
    def update_pipes(self):
        # Move Pipes
        for pipe in self.pipes:
            pipe.move(self.SCROLL_AMOUNT)
            if pipe.x < 0:
                del pipe
        
        # Add new pipe and reset pipe_clock
        if (abs(self.pipe_clock) >= 400):
                self.pipe_clock = 0
        if (self.pipe_clock == 0):
            self.pipes.append(Pipe.Pipe(self.WIDTH))
        self.pipe_clock = self.pipe_clock + self.SCROLL_AMOUNT

    def update_ground(self):
        self.ground.move(self.SCROLL_AMOUNT)

    ########## COLLISION HELPER FUNCTIONS ##########

    def is_collision(self, bird, pipe):
        return bird.mask.overlap(pipe.mask_top, (bird.x - pipe.x, bird.y - pipe.top_y - 600 + bird.curr_img.get_height())) \
        or bird.mask.overlap(pipe.mask_bottom, (bird.x - pipe.x, bird.y - pipe.bottom_y - 600 + bird.curr_img.get_height()))
    
    def ground_collision(self, bird):
        return bird.y >= 700 - bird.curr_img.get_height()