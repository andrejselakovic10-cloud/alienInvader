import pygame

class Ship:
    def __init__(self,screen):
        self.screen = screen
        self.ship = pygame.image.load("assets/ship.png")
        self.__shipPresentationSetup()
        self.speed = 1
        
    def __shipPresentationSetup(self):
        #SIZE
        scale = 0.25
        shipHeight = self.ship.get_height() * scale
        shipWidth = self.ship.get_width() * scale
        self.ship = pygame.transform.scale(self.ship,(shipWidth,shipHeight))
        #POSITION
        self.rect = self.ship.get_rect()
        self.rect.midbottom = self.screen.get_rect().midbottom
        #MOVEMENT
        self.movement = {"K_LEFT": False, "K_RIGHT": False, "K_UP": False, "K_DOWN": False, "SPACE": False}


    def __drawShip(self):
        self.screen.blit(self.ship, self.rect)

    def __handleMovement(self):
        if self.movement["K_LEFT"]:
            self.rect.x -= self.speed
        if self.movement["K_RIGHT"]:
            self.rect.x += self.speed
        if self.movement["K_DOWN"]:
            self.rect.y += self.speed 
        if self.movement["K_UP"]:
            self.rect.y -= self.speed 
    def handleShip(self):
        self.__drawShip()
        self.__handleMovement()

        