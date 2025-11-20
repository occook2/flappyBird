import pygame, os, math

class Ground:
    
    # Initializes the Ground object

    def __init__(self):
        self.IMG = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'imgs', 'base.png'))
        self.mask = pygame.mask.Mask((600, 100))
        self.x = 0
    
    # Displays the Ground object
    def display(self, screen, window_width):
        floor_tiles = math.ceil(window_width*2 / self.IMG.get_width()) + 1

        for i in range(0, floor_tiles):
                screen.blit(self.IMG,\
                            (i * self.IMG.get_width() + self.x ,700))
                
    def move(self, scroll):
         self.x -= scroll
         if (self.x < -600):
              self.x = 0
                
