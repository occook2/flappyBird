import pygame, os, time, random, math
import Ground, Pipe

# Window is used as the "Board" - will contain every object in the game
# and ensure the rules are followed. Game will contain a window along with
# other important information like score, etc.

class Window:

    def __init__(self):
        
        self.HEIGHT = 800
        self.WIDTH = 600
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
        scroll = 0

        # Start diplaying the window
        running = True
        while running:
            
            # Clock moves forward by FPS
            self.clock.tick(self.FPS)

            # Create multiple background images (instead of transforming width)
            bg_tiles = math.ceil(render_width / self.IMG.get_width())
            for i in range(0, bg_tiles):
                screen.blit(self.IMG, (i * self.IMG.get_width(),0))

            # Initialize and display the Ground
            ground = Ground.Ground()
            ground.display(screen, self.WIDTH, scroll)

            pipe = Pipe.Pipe(0)
            pipe.display(screen, self.WIDTH, scroll)

            # Scroll across, each frame move 3 pixels
            scroll -= 3
            if abs(scroll) > ground.IMG.get_width()*2:
                scroll = 0

            # Stop displaying the window and quit the game when X is clicked
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()
        pygame.quit()