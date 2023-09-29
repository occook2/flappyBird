import pygame, os, time, random, math, random
import Ground, Pipe, Bird

# Window is used as the "Board" - will contain every object in the game
# and ensure the rules are followed. Game will contain a window along with
# other important information like score, etc.

class Window:

    def __init__(self):
        
        self.HEIGHT = 800
        self.WIDTH = 600
        self.SCROLL_AMOUNT = 5
        self.IMG = pygame.image.load(os.path.join('imgs', 'bg.png'))
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.score = 0

        self.bird = Bird.Bird(125, 400)
        self.pipes = []
    
    def display(self):

        # Create window and transform background      
        screen = pygame.display.set_mode(size = (self.WIDTH, self.HEIGHT))
        self.IMG = pygame.transform.scale(self.IMG, (self.IMG.get_width(), self.HEIGHT))
        pygame.display.set_caption('BirdBaby.AI')
        pygame.display.flip()
        
        render_width = self.WIDTH*2
        ground_scroll = 0
        random_height = 450
        ground = Ground.Ground()
        
        pipe_scroll = 0

        # Start diplaying the window
        running = True
        while running:
            
            # Clock moves forward by FPS
            self.clock.tick(self.FPS)

            # Background Display
            bg_tiles = math.ceil(render_width / self.IMG.get_width())
            for i in range(0, bg_tiles):
                screen.blit(self.IMG, (i * self.IMG.get_width(),0))

            # Pipes Update and Display
            if (abs(pipe_scroll) >= 400):
                pipe_scroll = 0

            if (pipe_scroll == 0):
                random_height = self.get_random_pipe_height()
                self.pipes.append(Pipe.Pipe(600, random_height))

            self.pipes = self.update_and_display_pipes(self.pipes, self.SCROLL_AMOUNT, screen)
            pipe_scroll -= self.SCROLL_AMOUNT

            # Ground Update and Display
            ground.display(screen, self.WIDTH, ground_scroll)
            ground_scroll = self.update_ground_scroll(ground, ground_scroll)

            # Bird Update and Display
            self.bird.move()
            self.bird.display(screen)

            # Collision Detection
            bird_mask = pygame.mask.from_surface(self.bird.IMGS[0])
            pipe_masks = self.get_pipe_masks(self.pipes)

            for pipe_mask in pipe_masks:
                
                if bird_mask.overlap(pipe_mask[0], (self.bird.x - pipe_mask[1].x, \
                                                     self.bird.y - pipe_mask[2])):
                    running = False
                
            # Score Update
            for pipe in self.pipes:
                if self.bird.x > pipe.x + pipe.IMG_top.get_width() and pipe.passed == False:
                    self.score += 1
                    pipe.passed = True
                    

            # Stop displaying the window and quit the game when X is clicked
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.jump()

            pygame.display.update()

        del ground   
        pygame.quit()
        print("Final Score is " + str(self.score))
    

    ########## GROUND HELPER FUNCTIONS ##########
    def update_ground_scroll(self, ground, ground_scroll):
        ground_scroll -= self.SCROLL_AMOUNT
        if abs(ground_scroll) > ground.IMG.get_width()*2:
            ground_scroll = 0
        return ground_scroll

    ########## PIPE HELPER FUNCTIONS ##########
    def update_and_display_pipes(self, pipes, scroll, screen):
        for pipe in pipes:
                pipe.move(scroll) 
                pipe.display(screen)
                if pipe.x < 0:
                    del pipe
        return pipes
    
    def get_random_pipe_height(self):
        return int(math.ceil(random.uniform(0,1)*250) + 300)
    
    def get_pipe_masks(self, pipes):
        pipe_masks = []
        for pipe in pipes:
            pipe_masks.append((pygame.mask.from_surface(pipe.IMG_bottom), pipe, pipe.bottom_y + 600))
            pipe_masks.append((pygame.mask.from_surface(pipe.IMG_top), pipe, pipe.top_y + 600))
        return pipe_masks