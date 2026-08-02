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

                self._handleKeyEvents(event)

    def _handleKeyEvents(self, event):

        if event.type not in (pygame.KEYDOWN, pygame.KEYUP):
            return

        keyDown = False
        if event.type == pygame.KEYDOWN:
            keyDown = True                                
        if event.type == pygame.KEYUP:
            keyDown = False                                

        match event.key:
            case pygame.K_RIGHT:
                self.__ship.movement["K_RIGHT"] = keyDown                              
            case pygame.K_LEFT:
                self.__ship.movement["K_LEFT"] = keyDown                              
            case pygame.K_UP:
                self.__ship.movement["K_UP"] = keyDown                              
            case pygame.K_DOWN:
                self.__ship.movement["K_DOWN"] = keyDown                              

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
