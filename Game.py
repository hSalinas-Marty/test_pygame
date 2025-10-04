import pygame, sys
from pygame.locals import *

class Game:
    def __init__(self, pseudo) :
        self.pseudo = pseudo
    
    def run(self, fenetre):
        fenetre.fill("yellow")
        font = pygame.font.Font(None, 60)
        text = font.render(f"Bienvenue, {self.pseudo} !", True, (0, 0, 0))
        fenetre.blit(text, (100, 180))
        pygame.display.flip()
