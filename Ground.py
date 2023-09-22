import pygame, os

class Ground:
    self.IMG = pygame.image.load(os.path.join('imgs', 'base.png'))

    def __init__(self):
        