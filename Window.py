import pygame, os, time, random, math, random
import Ground, Pipe, Bird

# Window is used as the "Board" - will contain every object in the game
# and ensure the rules are followed. Game will contain a window along with
# other important information like score, etc.

class Window:

    HEIGHT = 800
    WIDTH = 600
    SCROLL_AMOUNT = 5
    IMG = pygame.image.load(os.path.join('imgs', 'bg.png'))
    FPS = 60

    def __init__(self):
        
        self.clock = pygame.time.Clock()
        self.score = 0

        # Bird and Pipes will probably need to be moved up to Game/AI Builder
        # Window will just display everything, AI will do things in the backend

        self.bird = Bird.Bird(125, 400)
        self.pipes = []
    
    def display(self, birds, pipes, score):

        # Create window and transform background      
        screen = pygame.display.set_mode(size = (self.WIDTH, self.HEIGHT))
        self.IMG = pygame.transform.scale(self.IMG, (self.IMG.get_width(), self.HEIGHT))
        pygame.display.set_caption('BirdBaby.AI')
        pygame.display.flip()
        
        render_width = self.WIDTH*2
        ground_scroll = 0
        random_height = 450
        ground = Ground.Ground()
        
        pipe_tick = 0

        # Start diplaying the window
        running = True
        while running:
            
            # Clock moves forward by FPS
            self.clock.tick(self.FPS)

            # Background Display
            self.background_display(screen, render_width)

            # Pipes Update and Display
            if (abs(pipe_tick) >= 400):
                pipe_tick = 0

            if (pipe_tick == 0):
                self.pipes.append(Pipe.Pipe(self.WIDTH))

            self.pipes = self.update_and_display_pipes(self.pipes, self.SCROLL_AMOUNT, screen)
            pipe_tick -= self.SCROLL_AMOUNT

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
    
    ########## BACKGROUND HELPER FUNCTIONS ##########

    def background_display(self, screen, render_width):
        bg_tiles = math.ceil(render_width / self.IMG.get_width())
        for i in range(0, bg_tiles):
            screen.blit(self.IMG, (i * self.IMG.get_width(),0))

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
    
    
    
    def get_pipe_masks(self, pipes):
        pipe_masks = []
        for pipe in pipes:
            pipe_masks.append((pygame.mask.from_surface(pipe.IMG_bottom), pipe, pipe.bottom_y + 600))
            pipe_masks.append((pygame.mask.from_surface(pipe.IMG_top), pipe, pipe.top_y + 600))
        return pipe_masks