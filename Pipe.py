import pygame, os, time, random, math

class Pipe:

    # Window will define the height of the pipe
    # Pipes will always be initialized on the right side of the screen
    def __init__(self, x):
        self.x = x
        self.height = self.get_random_pipe_height()
        self.bottom_y = 0
        self.top_y = 0
        self.gap = 175
        self.IMG_bottom = pygame.image.load(os.path.join('imgs', 'long pipe.png'))
        self.IMG_top = pygame.transform.flip(self.IMG_bottom, False, True)
        self.passed = False

        self.set_pipe_IMG_heights(self.height, self.gap)
    
    def display(self, screen):
        screen.blit(self.IMG_bottom, (self.x, self.bottom_y))
        screen.blit(self.IMG_top, (self.x, self.top_y))

    # Will decrease the x coordinate of the pipe
    def move(self, scroll):
        self.x -= scroll

    def get_mask(self):
        return (pygame.mask.from_surface(self.IMG_bottom), \
                pygame.mask.from_surface(self.IMG_top))
    
    ########## HELPER FUNCTIONS ##########
    def set_pipe_IMG_heights(self, height, gap):
        screen_w, screen_h = pygame.display.get_surface().get_size()
        self.bottom_y = screen_h - height + gap/2
        self.top_y = screen_h - height - gap/2 - self.IMG_top.get_height()

    def get_random_pipe_height(self):
        return int(math.ceil(random.uniform(0,1)*250) + 300)