import pygame, os, math

class Window:

    HEIGHT = 800
    WIDTH = 600
    SCROLL_AMOUNT = 5
    IMG = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'imgs', 'bg.png'))
    FPS = 60

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.screen = pygame.display.set_mode(size = (self.width, self.height))
        self.IMG = pygame.transform.scale(self.IMG, (self.IMG.get_width(), self.height))
    
    def display(self, birds, pipes, ground, score):  

        # Background Display
        self.background_display(self.screen, self.width)

        # Pipe display
        for pipe in pipes:
            pipe.display(self.screen)
        
        # Ground Update and Display
        ground.display(self.screen, self.width)

        # Bird Update and Display
        for bird in birds:
            bird.display(self.screen)
        
        pygame.font.init()
        STAT_FONT = pygame.font.SysFont("comicsans", 50)
        score_label = STAT_FONT.render("Score: " + str(score),1,(255,255,255))
        self.screen.blit(score_label, (self.width - score_label.get_width() - 15, 10))
 
    ########## BACKGROUND HELPER FUNCTIONS ##########
    def background_display(self, screen, render_width):
        bg_tiles = math.ceil(render_width / self.IMG.get_width())
        for i in range(0, bg_tiles):
            screen.blit(self.IMG, (i * self.IMG.get_width(),0))

    ########## GROUND HELPER FUNCTIONS ##########
    def update_ground_scroll(self, ground, ground_scroll):
        ground_scroll -= self.SCROLL_AMOUNT
        if abs(ground_scroll) > ground.IMG.get_width()*2:
            ground_scroll = 0
        return ground_scroll
   
    
    def get_pipe_masks(self, pipes):
        pipe_masks = []
        for pipe in pipes:
            pipe_masks.append((pygame.mask.from_surface(pipe.IMG_bottom), pipe, pipe.bottom_y + 600))
            pipe_masks.append((pygame.mask.from_surface(pipe.IMG_top), pipe, pipe.top_y + 600))
        return pipe_masks
    

    ########## STATS DISPLAY HELPER FUNCTIONS ##########