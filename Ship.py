import pygame

class Ship:
    def __init__(self,screen):
        self.screen = screen
        self.ship = pygame.image.load("assets/ship.png")
        self.shipSetup()
        self.left = False
        self.right = False
    def shipSetup(self):
    #sizeeee
        scale = 0.25
        shipHeight = self.ship.get_height() * scale
        shipWidth = self.ship.get_width() * scale
        self.ship = pygame.transform.scale(self.ship,(shipWidth,shipHeight))
    #postitonnnnnnnnn
        self.rect = self.ship.get_rect()
        self.rect.midbottom = self.screen.get_rect().midbottom

    def drawShip(self):
        self.screen.blit(self.ship, self.rect)
    def right(self):
        self.rect.x += 15
    def left(self):
        self.rect.x -= 15