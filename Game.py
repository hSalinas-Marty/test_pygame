import pygame
from pygame.locals import *

import Db

class Game:
    def __init__(self, pseudo, test, score = 0, niveau = 1) :
        self.pseudo = pseudo
        self.score = score
        self.niveau = niveau
        if test:
            self.data = Db.Database()                                                            # Creation Database
            self.data.sauvegarder_partie(self.pseudo, self.score, self.niveau)
    
    def run(self, fenetre):
        fenetre.fill("yellow")
        font = pygame.font.Font(None, 60)
        text = font.render(f"Bienvenue, {self.pseudo} !", True, (0, 0, 0))
        fenetre.blit(text, (100, 180))
        pygame.display.flip()


