import pygame
import sys
from Settings import Settings
from Ship import Ship
#SOLID - pravila
#S - single responsibilty - jedan klasa jedno zaduzenje

#Zaduzen samo za omogucavanje game loopa-a
class AlienInvaders:
    
    def __init__(self):
        pygame.init()
        
        self.__settings = Settings() 
        self.__screen = self.__settings.screen
        self.__ship = Ship(self.__screen)
    def __eventThings(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.__ship.right = True
                    if event.key == pygame.KEYUP:
                        self.__ship.right = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.__ship.left = True
                    if event.key == pygame.KEYUP:
                        self.__ship.left = False
    def __screenThings(self):
        self.__screen.fill(self.__settings.bg_color)
        self.__ship.drawShip()
        pygame.display.flip()
        
    def run_game(self):
        while True:
            self.__eventThings()
            self.__screenThings()
    
if __name__ == "__main__":
    ai = AlienInvaders() 
    ai.run_game()
