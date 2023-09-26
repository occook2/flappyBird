import pygame, os, time, random, math

class Pipe:

    # Window will define the dimensions of the next pipe (can randomize gap if needed)
    def __init__(self, height):
        self.height = height
        self.gap = 175
        self.IMG_bottom = pygame.image.load(os.path.join('imgs', 'long pipe.png'))
        self.IMG_top = pygame.transform.flip(self.IMG_bottom, False, True)
    
    def display(self, screen, window_width, scroll):
        screen_w, screen_h = pygame.display.get_surface().get_size()
        screen.blit(self.IMG_bottom, (window_width + scroll, screen_h - self.height + self.gap/2))
        screen.blit(self.IMG_top, (window_width + scroll, screen_h - self.height - 600 - self.gap/2))