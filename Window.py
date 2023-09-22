import pygame, os, time, random, math
import Ground

class Window:

    def __init__(self):
        
        self.HEIGHT = 800
        self.WIDTH = 600
        self.BGIMG = pygame.image.load(os.path.join('imgs', 'bg.png'))
        self.clock = pygame.time.Clock()
        self.FPS = 60

    def display(self):

        # Create window and transform background      
        screen = pygame.display.set_mode(size = (self.WIDTH, self.HEIGHT))
        self.BGIMG = pygame.transform.scale(self.BGIMG, (self.BGIMG.get_width(), self.HEIGHT))
        pygame.display.set_caption('BirdBaby.AI')
        pygame.display.flip()
        scroll = 0

        # Start diplaying the window
        running = True
        while running:
            
            # Clock moves forward by FPS
            self.clock.tick(self.FPS)

            # Create multiple background images (instead of transforming width)
            bg_tiles = math.ceil(self.WIDTH / self.BGIMG.get_width())
            for i in range(0, bg_tiles):
                screen.blit(self.BGIMG, (i * self.BGIMG.get_width(),0))

            # Initialize and display the Ground
            ground = Ground.Ground()
            ground.display(screen, self.WIDTH, scroll)

            # Scroll across, each frame move 3 pixels
            scroll -= 3
            if abs(scroll) > ground.BASEIMG.get_width():
                scroll = 0

            # Stop displaying the window and quit the game when X is clicked
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()
        pygame.quit()