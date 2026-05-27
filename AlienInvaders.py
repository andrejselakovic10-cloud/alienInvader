import pygame
import sys

class AlienInvaders:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invaders")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    sys.exit()                    




if __name__ == "__main__":
    ai = AlienInvaders() 
    ai.run_game()