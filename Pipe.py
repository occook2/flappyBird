import pygame, os, time, random, math

class Pipe:

    # Window needs to definte the height of the pipe (should be random)
    def __init__(self, height):
        self.height = height
        self.IMG = pygame.image.load(os.path.join('imgs', 'pipe.png'))
    
    def display(self, screen, window_width, scroll):
        screen_w, screen_h = pygame.display.get_surface().get_size()
        screen.blit(self.IMG, (window_width + scroll, screen_h - 420))