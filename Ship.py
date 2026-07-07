import pygame

class Ship:
    def __init__(self,screen):
        self.screen = screen
        self.ship = pygame.image.load("assets/ship.png")
        self.ship = pygame.transform.scale(self.ship,(200, 200))
        self.rect = self.ship.get_rect()
    def drawShip(self):
        self.screen.blit(self.ship, self.rect)
        