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
        self.pipes = [Pipe.Pipe(self.WIDTH)]
        self.pipe_clock = 0

        self.birds = []

        self.score = 0

    def play(self, genomes, config):

        nets = []
        ge = []

        for _, g in genomes:
            net = neat.nn.FeedForwardNetwork.create(g, config)
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

            # Exit Game Option
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()

            # Provide Input to Neural Nets and Receive Outputs
            next_pipe = 0
            if len(self.birds) > 0:
                for x, pipe in enumerate(self.pipes):
                    if not pipe.passed:
                        next_pipe = x
                        break
            else:
                running = False
                break

            for x, bird in enumerate(self.birds):
                ge[x].fitness += 0.1  # Every frame gives a small amount of fitness

                output = nets[x].activate((bird.y, \
                                          abs(bird.y - (self.pipes[next_pipe].height)), \
                                          abs(bird.y - (self.pipes[next_pipe].height + self.pipes[next_pipe].gap))))

                if output[0] > 0.98:
                    self.birds[x].jump()

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
                        ge.pop(x)
                        self.birds.pop(x)
                        nets.pop(x)

                    if not pipe.passed and bird.x > pipe.x + pipe.IMG_top.get_width(): # Change Pipe to Passed
                        for g in ge:
                            g.fitness += 5
                        pipe.passed = True
                        self.pipes.append(Pipe.Pipe(self.WIDTH))
                
                if self.ground_and_ceiling_collision(bird):
                    ge[x].fitness -= 1
                    ge.pop(x)
                    self.birds.pop(x)
                    nets.pop(x)

           
    
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
        
        self.pipe_clock = self.pipe_clock + self.SCROLL_AMOUNT

    def update_ground(self):
        self.ground.move(self.SCROLL_AMOUNT)

    ########## COLLISION HELPER FUNCTIONS ##########

    def is_collision(self, bird, pipe):
        return bird.mask.overlap(pipe.mask_top, (bird.x - pipe.x, bird.y - pipe.top_y - 600 + bird.curr_img.get_height())) \
        or bird.mask.overlap(pipe.mask_bottom, (bird.x - pipe.x, bird.y - pipe.bottom_y - 600 + bird.curr_img.get_height()))
    
    def ground_and_ceiling_collision(self, bird):
        return bird.y >= 700 - bird.curr_img.get_height() or bird.y < 0
    
    ########## AI HELPER FUNCTIONS ##########

    def delete_bird_and_neural_net(self, index, birds, nns, fitnesses):
        fitnesses[index].fitness -= 1
        fitnesses.pop(index)
        birds.pop(index)
        nns.pop(index)