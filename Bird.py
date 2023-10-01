import pygame, os

class Bird:

    IMGS = [pygame.image.load(os.path.join('imgs', 'bird1.png')), \
            pygame.image.load(os.path.join('imgs', 'bird2.png')), \
            pygame.image.load(os.path.join('imgs', 'bird3.png'))]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 0
        self.tick_count = 0
        self.img_count  = 0
        self.gravity = 0.1
        self.curr_img = self.IMGS[0]

    def display(self, screen):
        screen.blit(self.IMGS[self.img_count], (self.x, self.y))

    def jump(self):
        self.vel = -2
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

