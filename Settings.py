import pygame

class Settings: 
    def __init__(self):
        self.width = 1200
        self.height = 800
        self.bg_color = (250,0,0)
        self.game_title = "Alien Invaders"
        pygame.display.set_caption(self.game_title)
        self.screen = pygame.display.set_mode((self.width,self.height))

