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

        self.settings = Settings() #KOMPOZICIJA
        self.screen = self.settings.screen
        self.ship = Ship(self.screen)
        print(dir(self.ship))
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    sys.exit()       

            self.screen.fill(self.settings.bg_color)
            self.ship.drawShip()
            pygame.display.flip()
   

if __name__ == "__main__":
    ai = AlienInvaders() 
    ai.run_game()
