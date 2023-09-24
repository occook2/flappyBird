import pygame, os, time, random, math, random
import Ground, Pipe

# Window is used as the "Board" - will contain every object in the game
# and ensure the rules are followed. Game will contain a window along with
# other important information like score, etc.

class Window:

    def __init__(self):
        
        self.HEIGHT = 800
        self.WIDTH = 600
        self.SCROLL_AMOUNT = 3
        self.IMG = pygame.image.load(os.path.join('imgs', 'bg.png'))
        self.clock = pygame.time.Clock()
        self.FPS = 60

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
        
        pipes = []
        pipe_scroll = 0

        # Start diplaying the window
        running = True
        while running:
            
            # Clock moves forward by FPS
            self.clock.tick(self.FPS)

            # Create multiple background images (instead of transforming width)
            bg_tiles = math.ceil(render_width / self.IMG.get_width())
            for i in range(0, bg_tiles):
                screen.blit(self.IMG, (i * self.IMG.get_width(),0))

            # Create pipe every 400 pixels
            if (abs(pipe_scroll) >= 400):
                pipe_scroll = 0

            if (pipe_scroll == 0):
                random_height = math.ceil(random.uniform(0,1)*250) + 300
                pipes.append(Pipe.Pipe(random_height))

            for i in reversed(range(0, len(pipes))):
                temp_pipe_scroll = pipe_scroll - (len(pipes) - 1 - i) * 400 
                if abs(temp_pipe_scroll) > 800:
                    del pipes[0]
                else:
                    pipes[i].display(screen, self.WIDTH, temp_pipe_scroll)
            
            pipe_scroll -= self.SCROLL_AMOUNT

            # Display the Ground ad scroll by 3 pixels per frame
            ground.display(screen, self.WIDTH, ground_scroll)
            ground_scroll -= self.SCROLL_AMOUNT
            if abs(ground_scroll) > ground.IMG.get_width()*2:
                ground_scroll = 0

            # Stop displaying the window and quit the game when X is clicked
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()

        del ground   
        pygame.quit()