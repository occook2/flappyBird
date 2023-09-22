import pygame, os, time, random, math
import Ground

class Window:

    def __init__(self):

        self.HEIGHT = 800
        self.WIDTH = 600
        self.BGIMG = pygame.image.load(os.path.join('imgs', 'bg.png'))
        self.BASEIMG = pygame.image.load(os.path.join('imgs', 'base.png'))
        self.clock = pygame.time.Clock()
        self.FPS = 60

    def display(self):
        
        self.BGIMG = pygame.transform.scale(self.BGIMG, (self.WIDTH, self.HEIGHT))
        
        screen = pygame.display.set_mode(size = (self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('BirdBaby.AI')
        pygame.display.flip()

        scroll = 0

        running = True
        while running:
            
            self.clock.tick(self.FPS)

            screen.blit(self.BGIMG, (0,0))

            ground = Ground.Ground()
            ground.display(screen, self.WIDTH, scroll)

            scroll -= 3
            if abs(scroll) > self.BASEIMG.get_width():
                scroll = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()
        pygame.quit()