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

    def __handleEvents(self):
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()  

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.__ship.right = True                                
                    if event.key == pygame.K_LEFT:
                        self.__ship.left = True  
                    if event.key == pygame.K_UP:
                        self.__ship.up = True  
                    if event.key == pygame.K_DOWN:
                        self.__ship.down = True  
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.__ship.right = False                                
                    if event.key == pygame.K_LEFT:
                        self.__ship.left = False  
                    if event.key == pygame.K_UP:
                        self.__ship.up = False  
                    if event.key == pygame.K_DOWN:
                        self.__ship.down = False 

    def __drawScreen(self):
        # BACKGROUND COLOR
        self.__screen.fill(self.__settings.bg_color)
        
        # DRAW ELEMETS
        self.__ship.handleShip()

        # REFRESH
        pygame.display.flip()
        
    def run_game(self):
        while True:
            self.__handleEvents()
            self.__drawScreen()
    
if __name__ == "__main__":
    ai = AlienInvaders() 
    ai.run_game()
