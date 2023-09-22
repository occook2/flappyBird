import pygame, neat, os, time, random

WIN_WIDTH = 600
WIN_HEIGHT = 800


BIRD_IMGS = [pygame.image.load(os.path.join('imgs', 'bird1.png')), \
             pygame.image.load(os.path.join('imgs', 'bird2.png')), \
             pygame.image.load(os.path.join('imgs', 'bird3.png'))]
PIPE_IMG = pygame.image.load(os.path.join('imgs', 'pipe.png'))
FLOOR_IMG = pygame.image.load(os.path.join('imgs', 'base.png'))
BACKGROUND_IMG = pygame.image.load(os.path.join('imgs', 'bg.png'))

class Bird:
    IMGS = BIRD_IMGS

    def __init__(self, x, y):
        
        # Coordinate position of Bird
        self.x = x
        self.y = y
        self.height = self.y
        self.velocity = 0
        self.img_count = 0
        self.img = self.IMGS[0]
    
    def jump(self):
        self.velocity = -10
        self.height = self.y
        


