import pygame, os

class Bird:

    IMGS = [pygame.image.load(os.path.join('imgs', 'bird1.png')), \
            pygame.image.load(os.path.join('imgs', 'bird2.png')), \
            pygame.image.load(os.path.join('imgs', 'bird3.png'))]
    START_HEIGHT = 400
    X = 125

    def __init__(self):
        self.x = self.X
        self.y = self.START_HEIGHT
        self.vel = 0
        self.gravity = 0.5

        self.tick_count = 0
        self.img_count  = 0
        
        self.curr_img = self.IMGS[0]
        self.mask = pygame.mask.from_surface(self.curr_img)

        self.alive = True
        self.score = 0

    def display(self, screen):
        screen.blit(self.IMGS[self.img_count], (self.x, self.y))

    def jump(self):
        self.vel = -5
        self.tick_count = 0

    def move(self):
        self.tick_count += 1

        d = self.vel * self.tick_count + self.gravity*self.tick_count**2

        if d >= 11:
            d = 11
        
        self.y = self.y + d

    ########## MASK HELPER FUNCTIONS ##########

    def get_mask(self):
        return pygame.mask.from_surface(self.curr_img)

