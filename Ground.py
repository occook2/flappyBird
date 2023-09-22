import pygame, os, time, random, math

class Ground:

    def __init__(self):
        self.BASEIMG = pygame.image.load(os.path.join('imgs', 'base.png'))
    
    def display(self, screen, window_width, scroll):
        floor_tiles = math.ceil(window_width / self.BASEIMG.get_width()) + 1

        for i in range(0, floor_tiles):
                screen.blit(self.BASEIMG,\
                            (i * self.BASEIMG.get_width() + scroll ,700))